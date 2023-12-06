# SFU CMPT 340 Project Template -- Replace with project title
This repository is a template for your CMPT 340 course project.
Replace the title with your project title, and **add a snappy acronym that people remember (mnemonic)**.

This project focuses on the testing of multiple biomedical LLMs, with an aim of reproducing the results promised by their respective sources.

## Important Links

| [Timesheet](https://1sfu-my.sharepoint.com/:x:/g/personal/kabhishe_sfu_ca/EZ18ilpzUUFLubG8GtTbF6EB2QN-h6d7j62JO3VCog0bbA?e=TdwjVf) | [Slack channel](https://app.slack.com/client/T05JYJAF22G/C05TGR37XPW/docs/Qp:F05TT3JHM17) | [Project report](https://www.overleaf.com/project/650ca3406716f07f3579dc3e) |
|-----------|---------------|-------------------------|



## Video/demo/GIF
Record a short video (1:40 - 2 minutes maximum) or gif or a simple screen recording or even using PowerPoint with audio or with text, showcasing your work.


## Table of Contents
1. [Demo](#demo)

2. [Installation](#installation)

3. [Reproducing this project](#repro)

4. [Guidance](#guide)


<a name="demo"></a>
## 1. Example demo

A minimal example to showcase your work

```python
from transformers import pipeline, set_seed
from transformers import BioGptTokenizer, BioGptForCausalLM
model = BioGptForCausalLM.from_pretrained("microsoft/biogpt")
tokenizer = BioGptTokenizer.from_pretrained("microsoft/biogpt")
generator = pipeline('text-generation', model=model, tokenizer=tokenizer)
set_seed(42)
print(" ")
print("Output:")
print("------------------")
print(generator("COVID-19 is", max_length=100, num_return_sequences=1, do_sample=True))
print("------------------")
```

### What to find where


```bash
repository
├── llm-files/                        ## code from minimal example above: to run text generation with a prompt using BioGPT
    ├── bioMedCLIP.py                 ## code for BioMedCLIP LLM
    ├── BioMedLM.py                   ## code for BioMedLM LLM
    ├── biogpt-text-generation.py     ##code for text generation with bioGPT LLM
    ├── biogpt-question-answering.py  ##code for question answering with bioGPT LLM
    ├── gptneo-text-generation.py     ##code for text generation gptneo LLM
    ├── gptneo-question-answering.py  ##code for question answering gptneo LLM
    ├── meditron.py                   ##code for meditron LLM
    ├── openlm-test.py                ##code for openlm-test LLM
    ├── spacy-llm.py                  ##code for spacy-llm LLM
├── .py                               ## scripts, if needed
├── docs                              ## If needed, documentation   
├── README.md                         ## You are here
├── LLM-Guide.md                      ## md file containing installation and running instructions for each LLM
├── requirements.yml                  ## If you use conda
```

<a name="installation"></a>

## 2. Installation

Provide sufficient instructions to reproduce and install your project. 
Provide _exact_ versions, test on CSIL or reference workstations.

```bash
git clone https://github.com/Fredopayn1119/GROUP-22.git
cd GROUP-22
```

<a name="repro"></a>
## 3. Reproduction
Demonstrate how your work can be reproduced, e.g. the results in your report.
```bash
cd llm-files
python biogpt-text-generation.py
```
Output will be printed in the terminal.

<a name="guide"></a>
## 4. Guidance

- Use [git](https://git-scm.com/book/en/v2)
    - Do NOT use history re-editing (rebase)
    - Commit messages should be informative:
        - No: 'this should fix it', 'bump' commit messages
        - Yes: 'Resolve invalid API call in updating X'
    - Do NOT include IDE folders (.idea), or hidden files. Update your .gitignore where needed.
    - Do NOT use the repository to upload data
- Use [VSCode](https://code.visualstudio.com/) or a similarly powerful IDE
- Use [Copilot for free](https://dev.to/twizelissa/how-to-enable-github-copilot-for-free-as-student-4kal)
- Sign up for [GitHub Education](https://education.github.com/) 
