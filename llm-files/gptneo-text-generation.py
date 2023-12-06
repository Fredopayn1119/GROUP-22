#code here was referenced from BioGPT's instructions in the BioGPT GitHub. 

from transformers import pipeline, set_seed

generator = pipeline('text-generation', model='EleutherAI/gpt-neo-2.7B')
output = generator("COVID-19 is", max_length=50, num_beams=5)
set_seed(42)
print(" ")
print("Output:")
print("------------------")
print(output)
print("------------------")
