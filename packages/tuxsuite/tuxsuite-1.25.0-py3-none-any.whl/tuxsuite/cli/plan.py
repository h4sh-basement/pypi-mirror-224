# -*- coding: utf-8 -*-

from itertools import chain

import tuxsuite
import tuxsuite.cli.colors as colors
import tuxsuite.cli.icons as icons
from tuxsuite.cli.models import Plan
from tuxsuite.cli.requests import get, post
from tuxsuite.cli.common import common_options
from tuxsuite.cli.utils import (
    LIMIT,
    error,
    datediff,
    fetch_next,
    file_or_url,
    format_result,
    format_plan_result,
    show_log,
    wait_for_object,
    is_url,
)

import json
import sys


def format_plan(build, tests):
    if build.result == "pass":
        if build.warnings_count == 0:
            icon = icons.PASS
            message = "Pass"
            color = colors.green
        else:
            icon = icons.WARNING
            color = colors.yellow
            if build.warnings_count == 1:
                message = "Pass (1 warning)"
            else:
                message = "Pass ({} warnings)".format(build.warnings_count)
    elif build.result == "fail":
        icon = icons.FAIL
        color = colors.red
        if build.errors_count == 1:
            message = "Fail (1 error)"
        else:
            message = "Fail ({} errors)".format(build.errors_count)
    elif build.result == "error":
        icon = icons.ERROR
        color = colors.red
        message = build.status_message
    elif build.result == "canceled":
        icon = icons.CANCELED
        color = colors.white
        message = build.status_message
    elif build.result == "unknown":
        icon = icons.UNKNOWN
        color = colors.purple
        message = "Result unknown"
    else:
        raise NotImplementedError()

    builds = build.get_builds_message(icon, color, message)

    tests_str = ""
    tests_pass = sorted(
        set(chain.from_iterable([t.tests for t in tests if t.result == "pass"]))
    )
    tests_fail = sorted(
        set(chain.from_iterable([t.tests for t in tests if t.result == "fail"]))
    )
    tests_error = sorted(
        set(chain.from_iterable([t.tests for t in tests if t.result == "error"]))
    )
    tests_unknown = sorted(
        set(chain.from_iterable([t.tests for t in tests if t.result == "unknown"]))
    )
    tests_canceled = sorted(
        set(chain.from_iterable([t.tests for t in tests if t.result == "canceled"]))
    )
    if tests_pass:
        tests_str += (
            f" {icons.PASS} {colors.green}Pass: {','.join(tests_pass)}{colors.reset}"
        )
    if tests_fail:
        tests_str += (
            f" {icons.FAIL} {colors.red}Fail: {','.join(tests_fail)}{colors.reset}"
        )
    if tests_error:
        tests_str += (
            f" {icons.ERROR} {colors.red}Error: {','.join(tests_error)}{colors.reset}"
        )
    if tests_unknown:
        tests_str += f" {icons.UNKNOWN} {colors.purple}Unknown: {','.join(tests_unknown)}{colors.reset}"
    if tests_canceled:
        tests_str += f" {icons.CANCELED} {colors.white}Canceled: {','.join(tests_canceled)}{colors.reset}"

    return builds + tests_str


def format_test(test):
    if test.result == "pass":
        icon = icons.PASS
        color = colors.green
        message = "Pass"
    elif test.result == "fail":
        icon = icons.FAIL
        color = colors.red
        message = "Fail"
    elif test.result == "unknown":
        icon = icons.UNKNOWN
        color = colors.purple
        message = "Unknown"
    elif test.result == "canceled":
        icon = icons.CANCELED
        color = colors.white
        message = "Canceled"
    elif test.result == "error":
        icon = icons.ERROR
        color = colors.red
        message = "Error"
    else:
        raise NotImplementedError()

    return (
        test.uid
        + " "
        + f"test {icon} {color}{message}: {','.join(test.tests)}{colors.reset}"
    )


def handle_get(options, _, config):
    ret = get(
        config,
        f"/v1/groups/{config.group}/projects/{config.project}/plans/{options.uid}",
    )
    if ret.status_code == 404:
        err_msg = (
            f"\t{ret.json().get('error')}\n"
            "\tCheck if the plan's group/project are correct."
        )
        error(err_msg)

    if ret.status_code != 200:
        raise NotImplementedError()

    data = ret.json()

    start_builds = data["builds"]["next"]
    start_tests = data["tests"]["next"]
    start_oebuilds = data["oebuilds"]["next"]
    while start_builds or start_tests or start_oebuilds:
        ret = get(
            config,
            f"/v1/groups/{config.group}/projects/{config.project}/plans/{options.uid}",
            params={
                "start_builds": start_builds,
                "start_tests": start_tests,
                "start_oebuilds": start_oebuilds,
            },
        )
        if ret.status_code != 200:
            raise NotImplementedError()

        datan = ret.json()
        if start_builds:
            data["builds"]["results"].extend(datan["builds"]["results"])
            start_builds = datan["builds"]["next"]
        if start_tests:
            data["tests"]["results"].extend(datan["tests"]["results"])
            start_tests = datan["tests"]["next"]
        if start_oebuilds:
            data["oebuilds"]["results"].extend(datan["oebuilds"]["results"])
            start_oebuilds = datan["oebuilds"]["next"]

    plan = Plan.new(**data)
    if options.json:
        print(plan.as_json())
    else:
        print(
            f"{plan.provisioning_time[:-7]} {plan.uid} {plan.name} ({plan.description})"
        )

        for build in chain(
            plan.passing(),
            plan.warning(),
            plan.failing(),
            plan.errors(),
            plan.canceled(),
            plan.unknown(),
        ):
            print(format_plan(build, plan._tests_wait_for(build.uid)))
        # Print stand alone tests
        for test in [t for t in plan.tests if t.waiting_for is None]:
            print(format_test(test))

        bs = f"builds ({len(plan.all_builds)}):"
        provisioning = len(plan.filter_builds(lambda _, b: b.state == "provisioning"))
        running = len(plan.filter_builds(lambda _, b: b.state == "running"))
        passing = len(
            plan.filter_builds(
                lambda _, b: b.result == "pass" and b.warnings_count == 0
            )
        )
        warning = len(
            plan.filter_builds(
                lambda _, b: b.result == "pass" and b.warnings_count != 0
            )
        )
        failing = len(plan.filter_builds(lambda _, b: b.result == "fail"))
        err = len(plan.filter_builds(lambda _, b: b.result == "error"))
        canceled = len(plan.filter_builds(lambda _, b: b.result == "canceled"))
        unknown = len(plan.filter_builds(lambda _, b: b.result == "unknown"))

        if provisioning:
            bs += f" {icons.PROVISIONING} {provisioning}"
        if running:
            bs += f" {icons.RUNNING} {running}"
        if passing:
            bs += f" {icons.PASS} {passing}"
        if warning:
            bs += f" {icons.WARNING} {warning}"
        if failing:
            bs += f" {icons.FAIL} {failing}"
        if err:
            bs += f" {icons.ERROR} {err}"
        if canceled:
            bs += f" {icons.CANCELED} {canceled}"
        if unknown:
            bs += f" {icons.UNKNOWN} {unknown}"

        print(bs)

        ts = f"tests ({len(plan.tests)}):"
        waiting = len(plan.filter_tests(lambda _, t: t.state == "waiting"))
        provisioning = len(plan.filter_tests(lambda _, t: t.state == "provisioning"))
        running = len(plan.filter_tests(lambda _, t: t.state == "running"))
        passing = len(plan.filter_tests(lambda _, t: t.result == "pass"))
        failing = len(plan.filter_tests(lambda _, t: t.result == "fail"))
        err = len(plan.filter_tests(lambda _, t: t.result == "error"))
        canceled = len(plan.filter_tests(lambda _, t: t.result == "canceled"))
        unknown = len(plan.filter_tests(lambda _, t: t.result == "unknown"))

        if waiting:
            ts += f" {icons.WAITING} {waiting}"
        if provisioning:
            ts += f" {icons.PROVISIONING} {provisioning}"
        if running:
            ts += f" {icons.RUNNING} {running}"
        if passing:
            ts += f" {icons.PASS} {passing}"
        if failing:
            ts += f" {icons.FAIL} {failing}"
        if err:
            ts += f" {icons.ERROR} {err}"
        if canceled:
            ts += f" {icons.CANCELED} {canceled}"
        if unknown:
            ts += f" {icons.UNKNOWN} {unknown}"
        print(ts)
    return 0


def handle_cancel(options, _, config):
    ret = get(
        config,
        f"/v1/groups/{config.group}/projects/{config.project}/plans/{options.uid}",
    )
    if ret.status_code == 404:
        err_msg = (
            f"\t{ret.json().get('error')}\n"
            "\tCheck if the plan UID or group/project are correct."
        )
        error(err_msg)
    url = f"/v1/groups/{config.group}/projects/{config.project}/plans/{options.uid}/cancel"
    ret = post(config, url, data={})
    print(f"canceling plan {options.uid}")

    if ret.status_code != 200:
        print("plan not canceled")
        raise tuxsuite.exceptions.URLNotFound()

    return 0


def handle_wait(options, _, config):
    ret = get(
        config,
        f"/v1/groups/{config.group}/projects/{config.project}/plans/{options.uid}",
    )
    if ret.status_code != 200:
        raise NotImplementedError()

    data = ret.json()
    start_builds = data["builds"]["next"]
    start_tests = data["tests"]["next"]
    start_oebuilds = data["oebuilds"]["next"]
    while start_builds or start_tests or start_oebuilds:
        ret = get(
            config,
            f"/v1/groups/{config.group}/projects/{config.project}/plans/{options.uid}",
            params={
                "start_builds": start_builds,
                "start_tests": start_tests,
                "start_oebuilds": start_oebuilds,
            },
        )
        if ret.status_code != 200:
            raise NotImplementedError()
        datan = ret.json()
        if start_builds:
            data["builds"]["results"].extend(datan["builds"]["results"])
            start_builds = datan["builds"]["next"]
        if start_tests:
            data["tests"]["results"].extend(datan["tests"]["results"])
            start_tests = datan["tests"]["next"]
        if start_oebuilds:
            data["oebuilds"]["results"].extend(datan["oebuilds"]["results"])
            start_oebuilds = datan["oebuilds"]["next"]

    data["project"] = config.project
    plan = tuxsuite.Plan(config, **data)
    plan.plan = data["uid"]
    plan.load(plan.get_plan())
    if plan.builds:
        for build in plan.builds:
            build.build_data = f"{plan.url}/builds/{build.uid}"

    wait_for_object(plan)

    for b in chain(
        plan.passing(),
        plan.warning(),
        plan.failing(),
        plan.errors(),
        plan.canceled(),
        plan.unknown(),
    ):
        format_plan_result(b, plan._tests_wait_for(b.uid))
    return 0


def handle_list(options, _, config):
    url = f"/v1/groups/{config.group}/projects/{config.project}/plans"
    ret = get(config, url)
    if ret.status_code != 200:
        raise NotImplementedError()

    plans = [Plan.new(**p) for p in ret.json()["results"][: options.limit]]
    n_token = ret.json()["next"]
    if options.json:
        print(json.dumps([p.as_dict() for p in plans]))
    else:
        while True:
            previous_pt = None
            for plan in plans:
                pt = plan.provisioning_time
                if pt is None:
                    pt = "....-..-..T..:..:........."
                pt = pt[:-7]

                print(
                    f"{datediff(previous_pt, pt)} {plan.uid} {plan.name} ({plan.description})"
                )
                previous_pt = pt
            if sys.stdout.isatty():
                # fetch next list of plans
                plans, n_token = fetch_next(Plan, config, url, n_token, options.limit)
    return 0


def handle_submit(cmdargs, extra_arguments, config):
    if cmdargs.local_manifest and cmdargs.pinned_manifest:
        error("Either local manifest or pinned manifest to be provided, not both")

    if extra_arguments:
        error(f"Unknown option: {extra_arguments}")
        sys.exit(2)

    if cmdargs.git_head:
        try:
            cmdargs.git_repo, cmdargs.git_sha = tuxsuite.gitutils.get_git_head()
        except Exception as e:
            error(e)

    try:
        plan_config = tuxsuite.config.PlanConfig(
            cmdargs.name, cmdargs.description, cmdargs.config[0], cmdargs.job_name
        )

        # setting respective plan type class obj (Kernel or Bake)
        plan_type = plan_config.plan_type

        if plan_config.schema_warning:
            error(f"Invalid plan file: {plan_config.schema_warning}")

        if not plan_config.plan:
            error("Empty plan, skipping")
            return
        plan = tuxsuite.Plan(
            plan_config,
            git_repo=cmdargs.git_repo,
            git_sha=cmdargs.git_sha,
            git_ref=cmdargs.git_ref,
            patch_series=cmdargs.patch_series,
            no_cache=cmdargs.no_cache,
            manifest_file=cmdargs.local_manifest,
            pinned_manifest=cmdargs.pinned_manifest,
            is_public=cmdargs.private,
            kas_override=cmdargs.kas_override,
            lab=cmdargs.lab,
            lava_test_plans_project=cmdargs.lava_test_plans_project,
            callback=cmdargs.callback,
        )
    except (AssertionError, tuxsuite.exceptions.TuxSuiteError) as e:
        error(e)

    plan_type.plan_info(plan_config.name, plan_config.description)

    try:
        plan.submit()
        print("Plan {}/plans/{}\n".format(plan.url, plan.plan))
        print("uid: {}".format(plan.plan))
    except tuxsuite.exceptions.BadRequest as e:
        error(str(e))

    result = True

    if cmdargs.no_wait:
        for build in plan.builds:
            format_result(build.status, build.build_data)
        for test in plan.tests:
            format_result(test.status, plan.url + "/tests/{}".format(test.uid))
    else:
        result = wait_for_object(plan)
        print(f"\nSummary: {plan.url}/plans/{plan.plan}")
        for b in chain(
            plan.passing(),
            plan.warning(),
            plan.failing(),
            plan.errors(),
            plan.canceled(),
            plan.unknown(),
        ):
            format_plan_result(b, plan._tests_wait_for(b.uid))

    if cmdargs.json_out and plan.status:
        with open(cmdargs.json_out, "w") as json_out:
            json_out.write(json.dumps(plan.status, sort_keys=True, indent=4))
    if cmdargs.download:
        for build in plan.builds:
            tuxsuite.download.download(build, cmdargs.output_dir)
    if cmdargs.show_logs:
        for build in plan.builds:
            show_log(build, cmdargs.download, cmdargs.output_dir)

    if not result:
        sys.exit(1)


handlers = {
    "get": handle_get,
    "list": handle_list,
    "wait": handle_wait,
    "submit": handle_submit,
    "cancel": handle_cancel,
}


def plan_cmd_options(sp):
    sp.add_argument("--name", help="Set name")
    sp.add_argument("--description", help="Set description")
    sp.add_argument(
        "--job-name", action="append", help="Job name (may be specified multiple times)"
    )
    sp.add_argument(
        "--limit",
        default=LIMIT,
        help="Limit to LIMIT output. Used with [list]",
    )
    sp.add_argument(
        "--json",
        default=False,
        action="store_true",
        help="Show json output. Used with [get | list]",
    )
    sp.add_argument(
        "-l",
        "--local-manifest",
        default=None,
        help=(
            "Path to a local manifest file which will be used during repo sync. "
            "This input is ignored if sources used is git_trees in the build "
            "definition. Should be a valid XML. This option is only applicable in case of bake plan."
        ),
        type=file_or_url,
    )
    sp.add_argument(
        "-pm",
        "--pinned-manifest",
        default=None,
        help=(
            "Path to a pinned manifest file which will be used during repo sync. "
            "This input is ignored if sources used is git_trees in the build "
            "definition. Should be a valid XML. This option is only applicable in case of bake plan."
        ),
        type=file_or_url,
    )
    sp.add_argument(
        "-k",
        "--kas-override",
        type=file_or_url,
        default=None,
        help=(
            "Path to a kas config yml/yaml file which is appended to kas_yaml parameter."
            " This can be used to override the kas yaml file that is passed."
        ),
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
    # "plan get <uid>"
    p = parser.add_parser("get")
    p.add_argument("uid")
    p.add_argument("--json", action="store_true")

    # "plan list"
    p = parser.add_parser("list")
    p.add_argument("--json", action="store_true")
    p.add_argument("--limit", type=int, default=LIMIT)

    # "plan"
    t = parser.add_parser("submit")
    t.add_argument(
        "config",
        metavar="config",
        nargs=1,
        help="Plan config",
        const=None,
    )
    plan_cmd_options(t)
    common_options(t)

    # plan wait <uid>
    t = parser.add_parser("wait")
    t.add_argument("uid")

    # plan cancel <uid>
    t = parser.add_parser("cancel")
    t.add_argument("uid")

    return sorted(parser._name_parser_map.keys())
