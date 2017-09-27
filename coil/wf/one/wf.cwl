cwlVersion: v1.0
class: CommandLineTool
id: "random_lines"
doc: "Select random lines from a file"
inputs:
  - id: command
    type: string
    inputBinding:
      position: 1
  - id: seed
    type: int
    inputBinding:
      position: 2
      prefix: -s
  - id: input1
    type: File
    inputBinding:
      position: 3
  - id: num_lines
    type: int
    inputBinding:
      position: 4
  - id: output_file
    type: string
    inputBinding:
      position: 5
stdout: $(inputs.output_file)
outputs:
  - id: output
    type: File
    outputBinding:
      glob: $(inputs.output_file)
baseCommand: [ "random-lines" ]
#baseCommand: ["./random-lines"]
arguments: [$(inputs.seed) $(inputs.input1.path) $(inputs.num_lines) $(inputs.output_file)]
hints:
  SoftwareRequirement:
    packages:
    - package: 'random-lines'
      version:
      - '1.0'
