# Positional arguments

* `build-definition`: JSON file containing the build definition for OE build.

## Optional arguments

* `-l / local-manifest`: Path to a local manifest file which will be used during repo sync.This input is ignored if sources used is git_trees in the build definition.Should be a valid XML.

* `-pm / pinned-manifest`: Path to a pinned manifest file which will be used during repo sync.This input is ignored if sources used is git_trees in the build definition. Should be a valid XML.

* `-k / kas-override`: Path to a kas config yml/yaml file which is appended to kas_yaml parameter.This can be used to override the kas yaml file that is passed. This option is specific to kas builds.

* `-n / --no-wait`: Don't wait for the builds to finish

* `-d / --download`: Download artifacts after builds finish. Can't be used with no-wait

* `-o / --output-dir`: Directory where to download artifacts

* `-C / --no-cache`: Build without using any compilation cache

* `-P / --private`: Private build

* `--callback`: Callback URL. The bake backend will send a POST request to this URL with signed data, when bake completes.