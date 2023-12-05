from transformers import AutoTokenizer, AutoModelForCausalLM

tokenizer = AutoTokenizer.from_pretrained("epfl-llm/meditron-70b")
model = AutoModelForCausalLM.from_pretrained("epfl-llm/meditron-70b")

generator = pipeline('text-generation', model=model, tokenizer=tokenizer)
set_seed(42)
print(" ")
print("Output:")
print("------------------")
print(generator("COVID-19 is", max_length=100, num_return_sequences=1, do_sample=True))
print("------------------")