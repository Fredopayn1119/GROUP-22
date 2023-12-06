from transformers import pipeline, set_seed, AutoTokenizer, AutoModelForMaskedLM

tokenizer = AutoTokenizer.from_pretrained("microsoft/BiomedNLP-BiomedBERT-base-uncased-abstract-fulltext")
model = AutoModelForMaskedLM.from_pretrained("microsoft/BiomedNLP-BiomedBERT-base-uncased-abstract-fulltext")
generator = pipeline('text-generation', model=model, tokenizer=tokenizer)
set_seed(42)
print(" ")
print("Output:")
print("------------------")
print(generator("COVID-19 is ", max_length=100, num_return_sequences=1, do_sample=True))
print("------------------")
