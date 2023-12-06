#code here was referenced from BioGPT's instructions in the BioGPT GitHub. 

from transformers import pipeline, set_seed

generator = pipeline('question-answering', model='EleutherAI/gpt-neo-2.7B')
output = generator("What is COVID-19?", max_length=50, num_beams=5)
set_seed(42)
print(" ")
print("Output:")
print("------------------")
print(output)
print("------------------")
