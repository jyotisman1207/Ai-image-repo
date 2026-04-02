from transformers import pipeline
from PIL import Image

# Load captioning pipeline
captioner = pipeline("image-to-text", model="nlpconnect/vit-gpt2-image-captioning")

# Load image
image = Image.open("sample.jpg")

# Generate caption
result = captioner(image)

print("Generated Caption:", result[0]['generated_text'])
