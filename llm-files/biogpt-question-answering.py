
from transformers import pipeline, set_seed
from transformers import BioGptTokenizer, GPT2ForQuestionAnswering
model = GPT2ForQuestionAnswering.from_pretrained("microsoft/biogpt")
tokenizer = BioGptTokenizer.from_pretrained("microsoft/biogpt")
generator = pipeline('question-answering', model=model, tokenizer=tokenizer)
set_seed(42)
print(" ")
print("Output:")
print("------------------")
print(generator("What is COVID-19?", max_length=100, num_return_sequences=1, do_sample=True))
print("------------------")
