# -*- coding: utf-8 -*-

import pathlib
from tuxsuite.cli.utils import is_url


def common_options(sp):
    sp.add_argument(
        "-p",
        "--patch-series",
        default=None,
        help=(
            "Patches to apply before building the kernel. Accepts patch "
            "series that applies directly with 'git am' or "
            "'git quiltimport' i.e., a mbox file or directory or gzipped "
            "tarball (.tar.gz)"
        ),
    )
    sp.add_argument(
        "-s",
        "--show-logs",
        default=False,
        action="store_true",
        help="Prints build logs to stderr in case of warnings or errors",
    )
    sp.add_argument(
        "-n",
        "--no-wait",
        default=False,
        action="store_true",
        help="Don't wait for the builds to finish",
    )
    sp.add_argument(
        "-o",
        "--output-dir",
        default=".",
        help="Directory where to download artifacts",
    )
    sp.add_argument(
        "-d",
        "--download",
        default=False,
        action="store_true",
        help="Download artifacts after builds finish",
    )
    sp.add_argument(
        "--json-out",
        help="Write json build status out to a named file path",
        type=pathlib.Path,
    )
    sp.add_argument(
        "--git-head",
        default=False,
        action="store_true",
        help="Build the current git HEAD. Overrrides --git-repo and --git-ref",
    )
    sp.add_argument("--git-sha", help="Git commit")
    sp.add_argument("--git-ref", help="Git reference")
    sp.add_argument("--git-repo", help="Git repository")
    sp.add_argument(
        "-C",
        "--no-cache",
        default=False,
        action="store_true",
        help="Build without using any compilation cache",
    )
    sp.add_argument(
        "-P",
        "--private",
        default=True,
        action="store_false",
        help="Private build",
    )
    sp.add_argument(
        "--callback",
        default=None,
        help=(
            "Callback URL. Build/Test/Bake backend will send a POST "
            "request to this URL with signed data, when the respective build/test/bake "
            "completes."
        ),
        type=is_url,
    )
