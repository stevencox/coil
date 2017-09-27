import os

import cwltool.factory
import cwltool.draft2tool
from cwltool.draft2tool import CommandLineTool
import cwltool.workflow
from cwltool.process import get_feature, scandeps, UnsupportedRequirement, normalizeFilesDirs, shortname
from cwltool.load_tool import fetch_document
from cwltool.pathmapper import adjustFileObjs, adjustDirObjs, visit_class
from cwltool.utils import aslist
from cwltool.builder import substitute
from cwltool.pack import pack

# https://github.com/asher/chronos-python
# http://andrewjesaitis.com/2017/02/common-workflow-language---a-tutorial-on-making-bioinformatics-repeatable/

fac = cwltool.factory.Factory()

echo = fac.make("wf/one/wf.cwl")

result = echo(
    command = os.path.join (os.getcwd (), "wf", "one", "random-lines"),
    seed =  3,
    input1 = {
        "class"    : "File",
        "path"     : "wf/one/job.json",
        "contents" : "x099809808",
        "basename" : "random_lines_job.json"
    },
    num_lines = 40,
    output_file = "out.txt"
)


# result["out"] == "foo"

