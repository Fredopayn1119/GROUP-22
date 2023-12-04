from transformers import pipeline

# Example usage
generator = pipeline('text-generation', model='microsoft/BiomedCLIP-PubMedBERT_256-vit_base_patch16_224')
output = generator("COVID-19 is", max_length=50, num_beams=5)
print("Output:")
print("------------------")
print(output)
print("------------------")