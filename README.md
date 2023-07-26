# Prompt Evaluation
Evaluate metric on given input file

# Usage
run `python main.py -i INPUT -o OUTPUT -m METRIC -f FORMAT` to start
```python
usage: main.py [-h] -i INPUT -o OUTPUT [-m {rouge1,rouge2,rougeL} [{rouge1,rouge2,rougeL} ...]] [-f {json}]
options:
  -h, --help            show this help message and exit
  -i INPUT, --input INPUT
                        Path to input file
  -o OUTPUT, --output OUTPUT
                        Path to output file
  -m {rouge1, ...} [{rouge1}...], --metric {rouge1} [{rouge1} ...]
  -f {json}, --format {json}
```

# Example
`python main.py -i Testcase/test.json -o Testcase/output.json -m rouge1 rouge2 -f json`
This will calculate rouge1 rouge2 value on input file `Testcase/test.json`.
For input file format, you can take a look at `Testcase/test.json`. 
Or you can write your own class to support other format.
Notice that output format will be same as input format.

