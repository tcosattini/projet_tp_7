#!/bin/bash

project_root="$(dirname "$(dirname "$(readlink -f "${BASH_SOURCE}")")")"

find $project_root -name "__pycache__" -print0 | xargs -0 rm -rf