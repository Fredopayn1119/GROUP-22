# Instructions on reproducing LLMs

## Table of Contents

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

``` bash
python biogpt.py
```
An output containing the LLM's response to the prompt (the prompt being the first argument in the 'generator' function), should be printed in the terminal.


## LLM2
### Installation
### Running

## LLM3
### Installation
### Running


