import sys
import cwltool.factory

program, workflow_spec, job_spec, output_file = sys.argv
print ("workflow_spec: {0} job_spec: {1}".format (workflow_spec, job_spec))
factory = cwltool.factory.Factory ()
workflow = factory.make (workflow_spec)
args = { 
    "seed" :  3,
    "input1" : {
        "class"    : "File",
        "path"     : job_spec,
        "contents" : "x099809808",
        "basename" : "random_lines_job.json"
    },
    "num_lines"   : 40,
    "output_file" : output_file
}
workflow (**args)
