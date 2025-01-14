# -*- coding: utf-8 -*-

import tuxsuite
import tuxsuite.exceptions
import tuxsuite.cli.colors as colors
import tuxsuite.cli.icons as icons
from tuxsuite.cli.common import common_options
from tuxsuite.cli.models import Build
from tuxsuite.cli.requests import apiurl, get, post, headers
from tuxsuite.cli.utils import (
    LIMIT,
    datediff,
    fetch_next,
    key_value,
    wait_for_object,
    error,
    format_result,
    show_log,
)

import json
import requests
import sys
import time


def get_make_targets_vars(targets):
    target_list = []
    make_variables = {}
    if targets:
        key_values = [arg for arg in targets if "=" in arg]
        for kv in key_values:
            if kv.count("=") > 1:
                sys.stderr.write(f"Error: invalid KEY=VALUE: {kv}")
                sys.exit(1)
            make_variables = dict((arg.split("=") for arg in key_values))
        target_list = [arg for arg in targets if "=" not in arg]
    return (target_list, make_variables)


def handle_config(options, _, config):
    ret = get(
        config,
        f"/v1/groups/{config.group}/projects/{config.project}/builds/{options.uid}",
    )
    if ret.status_code != 200:
        raise NotImplementedError()

    # TODO: add a wrapper around requests.get
    ret = requests.get(f"{ret.json()['download_url']}config", headers=headers(config))
    if ret.status_code != 200:
        raise NotImplementedError()
    print(ret.text)
    return 0


def handle_get(options, _, config):
    ret = get(
        config,
        f"/v1/groups/{config.group}/projects/{config.project}/builds/{options.uid}",
    )
    if ret.status_code != 200:
        raise NotImplementedError()

    build = Build.new(**ret.json())
    if options.json:
        print(build.as_json())
    else:
        print(f"url      : {apiurl(config, build.url())}")
        print(f"project  : {build.project}")
        print(f"uid      : {build.uid}")
        print(f"plan     : {build.plan}")
        if build.waited_by:
            print(f"tests    : {', '.join([t.split('#')[1] for t in build.waited_by])}")
        print(f"user     : {build.user}")

        print(f"kconfig  : {', '.join(build.kconfig)}")
        print(f"target   : {build.target_arch}@{build.toolchain}")
        print(f"git repo : {build.git_repo}")
        print(f"git ref  : {build.git_ref}")
        print(f"git sha  : {build.git_sha}")
        print(f"git desc : {build.git_describe}")

        if build.provisioning_time:
            print(f"{icons.PROVISIONING} time  : {build.provisioning_time}")
        if build.running_time:
            print(f"{icons.RUNNING} time  : {build.running_time}")

        if build.state == "finished":
            if build.result == "pass" and build.warnings_count == 0:
                icon = icons.PASS
            elif build.result == "pass" and build.warnings_count != 0:
                icon = icons.WARNING
            elif build.result == "error":
                icon = icons.ERROR
            elif build.result == "fail":
                icon = icons.FAIL
            elif build.result == "unknown":
                icon = icons.UNKNOWN
            elif build.result == "canceled":
                icon = icons.CANCELED
            print(f"{icon} time  : {build.finished_time}")
        if build.duration:
            print(f"duration : {build.duration}")

        print(f"state    : {build.state}")
        color = ""
        if build.result == "pass":
            color = colors.green
        elif build.result == "canceled":
            color = colors.white
        elif build.result in ["error", "fail"]:
            color = colors.red
        elif build.result == "unknown":
            color = colors.purple
        print(f"result   : {color}{build.result}{colors.reset}")

        if build.errors_count:
            print(f"warnings : {colors.red}{build.errors_count}{colors.reset}")
        if build.warnings_count:
            print(f"warnings : {colors.yellow}{build.warnings_count}{colors.reset}")

    return 0


def handle_cancel(options, _, config):
    url = f"/v1/groups/{config.group}/projects/{config.project}/builds/{options.uid}/cancel"
    ret = post(config, url, data={})
    print(f"canceling job for {options.uid}")

    if ret.status_code != 200:
        print(f"unable to cancel build {options.uid}")
        raise tuxsuite.exceptions.URLNotFound()

    return 0


def handle_list(options, _, config):
    url = f"/v1/groups/{config.group}/projects/{config.project}/builds"
    ret = get(config, url)
    if ret.status_code != 200:
        raise NotImplementedError()

    builds = [Build.new(**b) for b in ret.json()["results"][: options.limit]]
    n_token = ret.json()["next"]
    if options.json:
        print(json.dumps([b.as_dict() for b in builds]))
    else:
        while True:
            previous_pt = None
            for build in builds:
                state = build.result if build.state == "finished" else build.state
                state_msg = (
                    f"{colors.state(build.state, build.result)}{state}{colors.reset}"
                )
                warnings = (
                    f" {colors.yellow}warnings={build.warnings_count}{colors.reset}"
                    if build.warnings_count
                    else ""
                )
                errors = (
                    f" {colors.red}errors={build.errors_count}{colors.reset}"
                    if build.errors_count
                    else ""
                )
                pt = build.provisioning_time
                if pt is None:
                    pt = "....-..-..T..:..:........."
                pt = pt[:-7]
                print(
                    f"{datediff(previous_pt, pt)} {build.uid} [{state_msg}] "
                    f"{build.target_arch}@{build.toolchain}{errors}{warnings}"
                )

                previous_pt = pt
            if sys.stdout.isatty():
                # fetch next list of builds
                builds, n_token = fetch_next(Build, config, url, n_token, options.limit)
    return 0


def handle_logs(options, _, config):
    ret = get(
        config,
        f"/v1/groups/{config.group}/projects/{config.project}/builds/{options.uid}",
    )
    if ret.status_code == 404:
        print(f"warning: {colors.red}Log unavailable{colors.reset}")
        return 0
    elif ret.status_code != 200:
        raise NotImplementedError()

    # TODO: add a wrapper around requests.get
    ret = requests.get(
        f"{ret.json()['download_url']}build.log", headers=headers(config)
    )
    if ret.status_code != 200:
        raise NotImplementedError()
    print(ret.text)
    return 0


def handle_wait(options, _, config):
    previous_state = None
    while True:
        ret = get(
            config,
            f"/v1/groups/{config.group}/projects/{config.project}/builds/{options.uid}",
        )
        if ret.status_code != 200:
            raise NotImplementedError()

        build = Build.new(**ret.json())
        if previous_state is None:
            previous_state = build.state
            print(f"url      : {apiurl(config, build.url())}")
            print(f"project  : {build.project}")
            print(f"uid      : {build.uid}")
            print(f"plan     : {build.plan}")
            if build.waited_by:
                print(
                    f"tests    : {', '.join([t.split('#')[1] for t in build.waited_by])}"
                )
            print(f"user     : {build.user}")

            print(f"kconfig  : {', '.join(build.kconfig)}")
            print(f"target   : {build.target_arch}@{build.toolchain}")
            print(f"git repo : {build.git_repo}")
            print(f"git ref  : {build.git_ref}")
            print(f"git sha  : {build.git_sha}")
            print(f"git desc : {build.git_describe}")

            if build.provisioning_time:
                print(f"{icons.PROVISIONING} time  : {build.provisioning_time}")
            if build.running_time:
                print(f"{icons.RUNNING} time  : {build.running_time}")

        if build.state != previous_state:
            if build.state == "provisioning":
                print(f"{icons.PROVISIONING} time  : {build.provisioning_time}")
            elif build.state == "running":
                print(f"{icons.RUNNING} time  : {build.running_time}")
            previous_state = build.state
        if build.state == "finished":
            break
        time.sleep(5)

    if build.result == "pass" and build.warnings_count == 0:
        icon = icons.PASS
    elif build.result == "pass" and build.warnings_count != 0:
        icon = icons.WARNING
    elif build.result == "error":
        icon = icons.ERROR
    elif build.result == "fail":
        icon = icons.FAIL
    elif build.result == "canceled":
        icon = icons.CANCELED
    elif build.result == "unknown":
        icon = icons.UNKNOWN

    print(f"{icon} time  : {build.finished_time}")
    if build.duration:
        print(f"duration : {build.duration}")

    print(f"state    : {build.state}")
    if build.result == "pass":
        color = colors.green
    elif build.result == "canceled":
        color = colors.white
    elif build.result == "unknown":
        color = colors.purple
    elif build.result in ["error", "fail"]:
        color = colors.red
    print(f"result   : {color}{build.result}{colors.reset}")

    if build.errors_count:
        print(f"warnings : {colors.red}{build.errors_count}{colors.reset}")
    if build.warnings_count:
        print(f"warnings : {colors.yellow}{build.warnings_count}{colors.reset}")

    return 0


def handle_submit(cmdargs, _, config):
    if cmdargs.git_head:
        try:
            cmdargs.git_repo, cmdargs.git_sha = tuxsuite.gitutils.get_git_head()
        except Exception as e:
            error(e)

    targets = ["config", "debugkernel", "dtbs", "kernel", "modules", "xipkernel"]
    make_variables = {}
    if cmdargs.targets[0]:
        target_list, make_vars = get_make_targets_vars(cmdargs.targets[0])
        targets = target_list
        make_variables = make_vars

    environment = {}
    for e in cmdargs.environment:
        environment[e[0][0]] = e[0][1]

    try:
        build = tuxsuite.Build(
            git_repo=cmdargs.git_repo,
            git_ref=cmdargs.git_ref,
            git_sha=cmdargs.git_sha,
            target_arch=cmdargs.target_arch,
            kconfig=cmdargs.kconfig,
            toolchain=cmdargs.toolchain,
            environment=environment,
            targets=targets,
            make_variables=make_variables,
            kernel_image=cmdargs.kernel_image,
            patch_series=cmdargs.patch_series,
            image_sha=cmdargs.image_sha,
            build_name=cmdargs.build_name,
            no_cache=cmdargs.no_cache,
            is_public=cmdargs.private,
            callback=cmdargs.callback,
        )

    except (AssertionError, tuxsuite.exceptions.TuxSuiteError) as e:
        error(e)
    print(
        "Building Linux Kernel {} at {}".format(
            build.git_repo, build.git_ref or build.git_sha
        )
    )
    try:
        build.build()
        print("uid: {}".format(build.uid))
    except tuxsuite.exceptions.BadRequest as e:
        error(e)

    build_result = True

    if cmdargs.no_wait:
        format_result(build.status, tuxapi_url=build.build_data)
    else:
        build_result = wait_for_object(build)

    if cmdargs.json_out and build.status:
        with open(cmdargs.json_out, "w") as json_out:
            json_out.write(json.dumps(build.status, sort_keys=True, indent=4))
    if cmdargs.download:
        tuxsuite.download.download(build, cmdargs.output_dir)
    if cmdargs.show_logs:
        show_log(build, cmdargs.download, cmdargs.output_dir)
    if cmdargs.quiet:
        print(build.build_data)

    if not build_result:
        sys.exit(1)


handlers = {
    "config": handle_config,
    "get": handle_get,
    "list": handle_list,
    "logs": handle_logs,
    "wait": handle_wait,
    "submit": handle_submit,
    "cancel": handle_cancel,
}


def build_cmd_options(sp):
    toolchains = [
        "gcc-8",
        "gcc-9",
        "gcc-10",
        "gcc-11",
        "gcc-12",
        "clang-10",
        "clang-11",
        "clang-12",
        "clang-13",
        "clang-14",
        "clang-15",
        "clang-16",
        "clang-nightly",
        "clang-android",
        "rust",
        "rustgcc",
        "rustclang",
        "rustllvm",
    ]

    sp.add_argument(
        "--build-name",
        help="User defined string to identify the build",
        type=str,
    )
    sp.add_argument(
        "targets",
        nargs="*",
        help="""Targets to build. If no TARGETs are specified, tuxsuite will
        build config + debugkernel + dtbs + kernel + modules + xipkernel.""",
        type=str,
        action="append",
    )
    sp.add_argument(
        "make-variables",
        nargs="*",
        help="Make variables to use. Format: KEY=VALUE",
        default=[],
        type=key_value,
        action="append",
    )
    sp.add_argument(
        "-e",
        "--environment",
        type=key_value,
        nargs="*",
        help="Set environment variables for the build. Format: KEY=VALUE",
        default=[],
        action="append",
    )
    sp.add_argument(
        "-q",
        "--quiet",
        default=False,
        action="store_true",
        help="Supress all informational output; prints only the download URL for the build",
    )
    sp.add_argument(
        "--toolchain",
        help=f"Toolchain [{'|'.join(toolchains)}]",
    )
    sp.add_argument(
        "--kconfig",
        nargs="?",
        help="Kernel kconfig arguments (may be specified multiple times)",
        type=str,
        default=[],
        action="append",
    )
    sp.add_argument(
        "--kernel-image",
        help="Specify custom kernel image that you wish to build",
    )
    sp.add_argument(
        "--target-arch",
        help="Target architecture [arc|arm|arm64|hexagon|i386|mips|parisc|powerpc|riscv|s390|sh|sparc|x86_64]",
    )
    sp.add_argument(
        "--image-sha",
        default=None,
        help="Pin the container image sha (64 hexadecimal digits)",
    )


def setup_parser(parser):
    # "build config <uid>"
    t = parser.add_parser("config")
    t.add_argument("uid")

    # "build get <uid>"
    p = parser.add_parser("get")
    p.add_argument("uid")
    p.add_argument("--json", action="store_true")

    # "build list"
    p = parser.add_parser("list")
    p.add_argument("--json", action="store_true")
    p.add_argument("--limit", type=int, default=LIMIT)

    # "build logs <uid>"
    t = parser.add_parser("logs")
    t.add_argument("uid")

    # "build submit"
    t = parser.add_parser("submit")
    build_cmd_options(t)
    common_options(t)

    # "build wait <uid>"
    p = parser.add_parser("wait")
    p.add_argument("uid")

    # "build cancel <uid>"
    t = parser.add_parser("cancel")
    t.add_argument("uid")

    return sorted(parser._name_parser_map.keys())
