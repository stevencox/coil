import cwltool.factory
#import cwltool.draft2tool
#import cwltool.workflow

import json
import os
import requests
#from cwltool.draft2tool import CommandLineTool
#from cwltool.process import get_feature, scandeps, UnsupportedRequirement, normalizeFilesDirs, shortname
#from cwltool.load_tool import fetch_document
#from cwltool.pathmapper import adjustFileObjs, adjustDirObjs, visit_class
#from cwltool.utils import aslist
#from cwltool.builder import substitute
#from cwltool.pack import pack
from stars import Stars

# https://github.com/asher/chronos-python
# http://andrewjesaitis.com/2017/02/common-workflow-language---a-tutorial-on-making-bioinformatics-repeatable/
# https://github.com/curoverse/arvados/blob/master/sdk/cwl/arvados_cwl/runner.py
# PATH=$PWD/wf/one:$PATH python app.py

class Coil(object):

    def __init__(self):
        self.factory = cwltool.factory.Factory ()

    def execute (self, workflow_spec, args={}):
        return self.factory.make (workflow_spec) (**args)

Coil ().execute (
    workflow_spec = "wf/one/wf.cwl",
    args = { 
        "seed" :  3,
        "input1" : {
            "class"    : "File",
            "path"     : "wf/one/job.json",
            "contents" : "x099809808",
            "basename" : "random_lines_job.json"
        },
        "num_lines"   : 40,
        "output_file" : "out.txt"
    })
