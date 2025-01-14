# -*- coding: utf-8 -*-

import pathlib
import tuxsuite
import tuxsuite.exceptions
import tuxsuite.cli.colors as colors
import tuxsuite.cli.icons as icons
from tuxsuite.cli.models import Test
from tuxsuite.cli.requests import apiurl, get, post
from tuxsuite.cli.utils import (
    LIMIT,
    datediff,
    fetch_next,
    key_value,
    wait_for_object,
    format_result,
    error,
    is_url,
)
from tuxsuite.cli.yaml import yaml_load

import json
import sys
import time


COLORS = {
    "exception": "\033[1;31m",
    "error": "\033[1;31m",
    "warning": "\033[1;33m",
    "info": "\033[1;37m",
    "debug": "\033[0;37m",
    "target": "\033[32m",
    "input": "\033[0;35m",
    "feedback": "\033[0;33m",
    "results": "\033[1;34m",
    "dt": "\033[0;90m",
    "end": "\033[0m",
}


def handle_get(options, _, config):
    ret = get(
        config,
        f"/v1/groups/{config.group}/projects/{config.project}/tests/{options.uid}",
    )
    if ret.status_code != 200:
        raise NotImplementedError()

    test = Test.new(**ret.json())
    if options.json:
        print(test.as_json())
    else:
        print(f"url     : {apiurl(config, test.url())}")
        print(f"project : {test.project}")
        print(f"uid     : {test.uid}")
        print(f"plan    : {test.plan}")
        if test.waiting_for:
            kind, waiting_for = test.waiting_for.split("#")
            print(
                f"build   : {waiting_for}"
                if kind == "BUILD"
                else f"test    : {waiting_for}"
            )
        print(f"user    : {test.user}")

        print(f"device  : {test.device}")
        print(f"kernel  : {test.kernel}")
        print(f"modules : {test.modules}")
        print(f"bootargs: {test.boot_args}")
        print(f"tests   : {', '.join(test.tests)}")
        print(f"overlays : {test.overlays}")

        if test.provisioning_time:
            print(f"{icons.PROVISIONING} time : {test.provisioning_time}")
        if test.running_time:
            print(f"{icons.RUNNING} time : {test.running_time}")

        if test.state == "finished":
            if test.result == "pass":
                icon = icons.PASS
            elif test.result == "error":
                icon = icons.ERROR
            elif test.result == "fail":
                icon = icons.FAIL
            elif test.result == "canceled":
                icon = icons.CANCELED
            elif test.result == "unknown":
                icon = icons.UNKNOWN
            print(f"{icon} time : {test.finished_time}")
        if test.duration:
            print(f"duration: {test.duration}")

        print(f"state   : {test.state}")
        color = ""
        if test.result == "pass":
            color = colors.green
        elif test.result in ["error", "fail"]:
            color = colors.red
        elif test.result == "canceled":
            color = colors.white
        elif test.result == "unknown":
            color = colors.purple
        print(f"result  : {color}{test.result}{colors.reset}")
    return 0


def handle_cancel(options, _, config):
    url = f"/v1/groups/{config.group}/projects/{config.project}/tests/{options.uid}/cancel"
    ret = post(config, url, data={})
    print(f"canceling job for {options.uid}")

    if ret.status_code != 200:
        print(f"unable to cancel test {options.uid}")
        raise tuxsuite.exceptions.URLNotFound()

    return 0


def handle_list(options, _, config):
    url = f"/v1/groups/{config.group}/projects/{config.project}/tests"
    ret = get(config, url)
    if ret.status_code != 200:
        raise NotImplementedError()

    tests = [Test.new(**t) for t in ret.json()["results"][: options.limit]]
    n_token = ret.json()["next"]
    if options.json:
        print(json.dumps([t.as_dict() for t in tests]))
    else:
        while True:
            previous_pt = None
            for test in tests:
                state = test.result if test.state == "finished" else test.state
                state_msg = (
                    f"{colors.state(test.state, test.result)}{state}{colors.reset}"
                )
                all_tests = ",".join(test.tests)
                pt = test.provisioning_time
                if pt is None:
                    pt = "....-..-..T..:..:........."
                pt = pt[:-7]
                print(
                    f"{datediff(previous_pt, pt)} {test.uid} [{state_msg}] {all_tests}@{test.device} {test.kernel}"
                )

                previous_pt = pt
            if sys.stdout.isatty():
                # fetch next list of tests
                tests, n_token = fetch_next(Test, config, url, n_token, options.limit)
    return 0


def handle_logs(options, _, config):
    ret = get(
        config,
        f"/v1/groups/{config.group}/projects/{config.project}/tests/{options.uid}/logs/lava",
    )
    if ret.status_code != 200:
        raise NotImplementedError()

    if options.raw:
        print(ret.text)
        return 0

    data = yaml_load(ret.text)
    for line in data:
        level = line["lvl"]
        msg = line["msg"]
        timestamp = line["dt"].split(".")[0]

        print(
            f"{COLORS['dt']}{timestamp}{COLORS['end']} {COLORS[level]}{msg}{COLORS['end']}"
        )
    return 0


def handle_results(options, _, config):
    ret = get(
        config,
        f"/v1/groups/{config.group}/projects/{config.project}/tests/{options.uid}/results",
    )
    if ret.status_code != 200:
        raise NotImplementedError()

    if options.raw:
        print(ret.text)
        return 0

    data = json.loads(ret.text)
    for k1, v2 in data.items():
        for k2, v2 in v2.items():
            if v2["result"] == "pass":
                print(f"{k1}.{k2}: {colors.green}{v2['result']}{colors.reset}")
            elif v2["result"] == "fail":
                print(f"{k1}.{k2}: {colors.red}{v2['result']}{colors.reset}")
            elif v2["result"] == "canceled":
                print(f"{k1}.{k2}: {colors.white}{v2['result']}{colors.reset}")
            elif v2["result"] == "unknown":
                print(f"{k1}.{k2}: {colors.purple}{v2['result']}{colors.reset}")
            else:
                print(f"{k1}.{k2}: {v2['result']}")
    return 0


def handle_wait(options, _, config):
    previous_state = None
    while True:
        ret = get(
            config,
            f"/v1/groups/{config.group}/projects/{config.project}/tests/{options.uid}",
        )
        if ret.status_code != 200:
            raise NotImplementedError()

        test = Test.new(**ret.json())
        if previous_state is None:
            previous_state = test.state
            print(f"url     : {apiurl(config, test.url())}")
            print(f"project : {test.project}")
            print(f"uid     : {test.uid}")
            print(f"plan    : {test.plan}")
            if test.waiting_for:
                kind, waiting_for = test.waiting_for.split("#")
                print(
                    f"build   : {waiting_for}"
                    if kind == "BUILD"
                    else f"test    : {waiting_for}"
                )
            print(f"user    : {test.user}")

            print(f"device  : {test.device}")
            print(f"kernel  : {test.kernel}")
            print(f"modules : {test.modules}")
            print(f"bootargs: {test.boot_args}")
            print(f"tests   : {', '.join(test.tests)}")
            print(f"overlays : {test.overlays}")
            if test.provisioning_time:
                print(f"{icons.PROVISIONING} time : {test.provisioning_time}")
            if test.running_time:
                print(f"{icons.RUNNING} time : {test.running_time}")

        if test.state != previous_state:
            if test.state == "provisioning":
                print(f"{icons.PROVISIONING} time : {test.provisioning_time}")
            elif test.state == "running":
                print(f"{icons.RUNNING} time : {test.running_time}")
            previous_state = test.state
        if test.state == "finished":
            break
        time.sleep(5)

    if test.result == "pass":
        icon = icons.PASS
    elif test.result == "error":
        icon = icons.ERROR
    elif test.result == "fail":
        icon = icons.FAIL
    elif test.result == "canceled":
        icon = icons.CANCELED
    elif test.result == "unknown":
        icon = icons.UNKNOWN
    print(f"{icon} time : {test.finished_time}")

    if test.duration:
        print(f"duration: {test.duration}")

    print(f"state   : {test.state}")
    if test.result == "pass":
        color = colors.green
    elif test.result in ["error", "fail"]:
        color = colors.red
    elif test.result == "canceled":
        color = colors.white
    elif test.result == "unknown":
        color = colors.purple
    print(f"result  : {color}{test.result}{colors.reset}")
    return 0


def handle_submit(cmdargs, _, config):
    if not cmdargs.device:
        error("--device is a required argument")

    tests = [test for test in cmdargs.tests.split(",") if test]
    tests = [test for test in tests if test != "boot"]
    if cmdargs.wait_for:
        print(
            "Testing build {} on {} with {}".format(
                cmdargs.wait_for, cmdargs.device, ", ".join(["boot"] + tests)
            )
        )
        if cmdargs.kernel:
            error("--kernel and --wait-for are mutually exclusive")
        if cmdargs.modules:
            error("--modules and --wait-for are mutually exclusive")
    else:
        print(
            "Testing {} on {} with {}".format(
                cmdargs.kernel, cmdargs.device, ", ".join(["boot"] + tests)
            )
        )

    params = {}
    for p in cmdargs.parameters:
        params[p[0][0]] = p[0][1]

    timeouts_d = {}
    for t in cmdargs.timeouts:
        timeouts_d[t[0][0]] = int(t[0][1])

    try:
        test = tuxsuite.Test(
            ap_romfw=cmdargs.ap_romfw,
            bios=cmdargs.bios,
            boot_args=cmdargs.boot_args,
            device=cmdargs.device,
            dtb=cmdargs.dtb,
            fip=cmdargs.fip,
            kernel=cmdargs.kernel,
            mcp_fw=cmdargs.mcp_fw,
            mcp_romfw=cmdargs.mcp_romfw,
            modules=cmdargs.modules,
            overlays=cmdargs.overlays,
            parameters=params,
            rootfs=cmdargs.rootfs,
            scp_fw=cmdargs.scp_fw,
            scp_romfw=cmdargs.scp_romfw,
            tests=tests,
            timeouts=timeouts_d,
            wait_for=cmdargs.wait_for,
            callback=cmdargs.callback,
            commands=cmdargs.commands,
            qemu_image=cmdargs.qemu_image,
            tuxbuild=cmdargs.tuxbuild,
            lab=cmdargs.lab,
            lava_test_plans_project=cmdargs.lava_test_plans_project,
        )
    except (AssertionError, tuxsuite.exceptions.TuxSuiteError) as e:
        error(e)

    try:
        test.test()
        print("uid: {}".format(test.uid))
    except tuxsuite.exceptions.BadRequest as e:
        error(str(e))

    test_result = True

    if cmdargs.no_wait:
        format_result(test.status, test.url)
    else:
        test_result = wait_for_object(test)

    if cmdargs.json_out and test.status:
        with open(cmdargs.json_out, "w") as json_out:
            json_out.write(json.dumps(test.status, sort_keys=True, indent=4))

    # If the test did not pass, exit with exit code of 1
    if not test_result:
        sys.exit(1)


handlers = {
    "get": handle_get,
    "list": handle_list,
    "logs": handle_logs,
    "results": handle_results,
    "submit": handle_submit,
    "wait": handle_wait,
    "cancel": handle_cancel,
}


def test_cmd_options(sp):
    sp.add_argument(
        "--device",
        help="Device type",
        type=str,
    )
    sp.add_argument(
        "--kernel",
        help="URL of the kernel to test",
        default=None,
        type=str,
    )
    sp.add_argument(
        "--bios",
        help="URL of the bios to test",
        default=None,
        type=str,
    )
    sp.add_argument(
        "--dtb",
        help="URL of the dtb to test",
        default=None,
        type=str,
    )
    sp.add_argument(
        "--mcp-fw", help="URL of the MCP firmware to test", default=None, type=str
    )
    sp.add_argument(
        "--mcp-romfw",
        help="URL of the MCP ROM firmware to test",
        default=None,
        type=str,
    )
    sp.add_argument(
        "--modules",
        help="URL of the kernel modules",
        default=None,
        type=str,
    )
    sp.add_argument(
        "--rootfs",
        help="URL of the rootfs to test",
        default=None,
        type=str,
    )
    sp.add_argument(
        "--scp-fw", help="URL of the SCP firmware to test", default=None, type=str
    )
    sp.add_argument(
        "--ap-romfw",
        help="URL of the AP ROM firmware to test",
        default=None,
        type=str,
    )
    sp.add_argument(
        "--scp-romfw",
        help="URL of the SCP ROM firmware to test",
        default=None,
        type=str,
    )
    sp.add_argument("--fip", help="URL of the fip.bin to test", default=None, type=str)
    sp.add_argument(
        "--overlay",
        default=[],
        metavar="URL",
        type=is_url,
        help="Tarball with overlay for rootfs. Can be specified multiple times",
        action="append",
        dest="overlays",
    )
    sp.add_argument(
        "--parameters",
        help="test parameters as KEY=VALUE",
        default=[],
        type=key_value,
        nargs="*",
        action="append",
    )
    sp.add_argument(
        "--tests",
        help="Comma separated list of tests",
        default="boot",
        type=str,
    )
    sp.add_argument(
        "--timeouts",
        help="timeouts as KEY=VALUE",
        default=[],
        type=key_value,
        nargs="*",
        action="append",
    )
    sp.add_argument(
        "--boot-args",
        help="Extra boot arguments",
        default=None,
        type=str,
    )
    sp.add_argument(
        "--wait-for",
        help="Wait for a test uid",
        default=None,
        type=str,
    )
    sp.add_argument(
        "-n",
        "--no-wait",
        default=False,
        action="store_true",
        help="Don't wait for tests to finish",
    )
    sp.add_argument(
        "--json-out",
        help="Write json test status out to a named file path",
        type=pathlib.Path,
    )
    sp.add_argument(
        "--callback",
        default=None,
        help=(
            "Callback URL. The test backend will send a POST request "
            "to this URL with signed data, when the test completes."
        ),
        type=is_url,
    )
    sp.add_argument(
        "--commands",
        nargs="*",
        help="Space separated list of commands to run inside the VM",
        default=[],
    )
    sp.add_argument(
        "--qemu-image",
        default=None,
        help="Use qemu from the given container image",
    )
    sp.add_argument(
        "--tuxbuild",
        metavar="URL",
        default=None,
        help="URL of a TuxBuild build",
        type=is_url,
    )
    sp.add_argument(
        "--lab",
        metavar="URL",
        default="https://lkft.validation.linaro.org",
        help="URL of LAVA lab instance",
        type=is_url,
    )
    sp.add_argument(
        "--lava-test-plans-project",
        default=None,
        help="Lava test plans project name",
        type=str,
    )


def setup_parser(parser):
    # "test get <uid>"
    t = parser.add_parser("get")
    t.add_argument("uid")
    t.add_argument("--json", action="store_true")

    # "test list"
    t = parser.add_parser("list")
    t.add_argument("--json", action="store_true")
    t.add_argument("--limit", type=int, default=LIMIT)

    # "test logs <uid>"
    t = parser.add_parser("logs")
    t.add_argument("uid")
    t.add_argument("--raw", action="store_true")

    # "test results <uid>"
    t = parser.add_parser("results")
    t.add_argument("uid")
    t.add_argument("--raw", action="store_true")

    # "test submit"
    t = parser.add_parser("submit")
    test_cmd_options(t)

    # "test wait <uid>"
    t = parser.add_parser("wait")
    t.add_argument("uid")

    # "test cancel <uid>"
    t = parser.add_parser("cancel")
    t.add_argument("uid")

    return sorted(parser._name_parser_map.keys())
