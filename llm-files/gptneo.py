#code here was referenced from BioGPT's instructions in the BioGPT GitHub. 

from transformers import pipeline

generator = pipeline('text-generation', model='EleutherAI/gpt-neo-2.7B')
output = generator("COVID-19 is", max_length=100, num_beams=5)
print(output)
