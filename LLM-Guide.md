# Instructions on reproducing LLM results

## Table of Contents

1. [Initial Setup](#initial-setup)

2. [BioGPT](#biogpt)

3. [GPTNeo](#gptneo)



## Initial Setup

For all of the LLMs below, Visual Studio Code was the code editor of choice. It is strongly recommended that this be the code editor used, as all the instructions are written assuming that this is code editor the reader will be using to follow along.

Before jumping into any of the LLMs, ensure that the Python extension for Visual Studio Code has been installed:

<p align=center>
  <img src="images/Extension-button.png" width=350 title="hover text">
  <img src="images/Python-Extension.png" width=500 alt="accessibility text">
</p>

Next, clone the repository:
``` bash
git clone https://github.com/Fredopayn1119/GROUP-22.git
cd GROUP-22
```

Finally, pip (a package manager) must be installed:

``` bash
python -m ensurepip --upgrade
```

## BioGPT
### Installation
Install the transformers library, which includes some of the APIs that will be used in the code:

``` bash
pip install transformers
```

### Running
Now, the code for BioGPT is ready to be executed!
For text generation:

``` bash
cd llm-files
python biogpt-text-generation.py
```
An output containing the LLM's response to the prompt (the prompt being the first argument in the 'generator' function), should be printed in the terminal.

For question answering:

``` bash
cd llm-files
python biogpt-question-answering.py
```
An output containing the LLM's response to the prompt (the prompt being the first argument in the 'generator' function), should be printed in the terminal.


## GPTNeo
### Installation
Install the transformers library, which includes some of the APIs that will be used in the code:

``` bash
pip install transformers
```

### Running
Now, the code for GPTNeo is ready to be executed!
For text generation:

``` bash
cd llm-files
python gptneo-text-generation.py
```
An output containing the LLM's response to the prompt (the prompt being the first argument in the 'generator' function), should be printed in the terminal.

For question answering:

``` bash
cd llm-files
python gptneo-question-answering.py
```

## BioMedLM
### Installation
### Running

## PubMedBERT
## GPTNeo
### Installation
Install the transformers library, which includes some of the APIs that will be used in the code:

``` bash
pip install transformers
```

### Running
Now, the code for GPTNeo is ready to be executed!

``` bash
cd llm-files
python pubmedbert.py
```

## BioBERT
### Installation
``` bash
git clone https://github.com/dmis-lab/biobert-pytorch.git
cd biobert-pytorch
pip install transformers==3.0.0
./download.sh
```
### Running
N/A - was not able to install (refer to problem description in report)

## Meditron
### Installation
Install the transformers library, which includes some of the APIs that will be used in the code:

``` bash
pip install transformers
```

### Running
Now, the code for Meditron is ready to be executed!

``` bash
cd llm-files
python meditron.py
```
An output containing the LLM's response to the prompt (the prompt being the first argument in the 'generator' function), should be printed in the terminal (if the device this code is executed on has enough storage space).



