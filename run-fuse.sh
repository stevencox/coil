#!/bin/bash

set -x
set -e

PATH=$PWD/wf/one:$PATH
export PYTHONPATH=/projects/stars/app/cwltool
export PYTHONPATH=/projects/stars/app/stars/cluster/src/stars:$PYTHONPATH
DATA_ROOT=irods

python app.py "$DATA_ROOT/wf/one/wf.cwl" "$DATA_ROOT/wf/one/job.json" "$DATA_ROOT/wf/one/out.txt"

exit 0
