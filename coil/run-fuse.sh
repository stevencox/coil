#!/bin/bash

set -x
set -e

PATH=$PWD/wf/one:$PATH
export PYTHONPATH=/projects/stars/app/cwltool
export PYTHONPATH=/projects/stars/app/stars/cluster/src/stars:$PYTHONPATH

python app.py

exit 0
