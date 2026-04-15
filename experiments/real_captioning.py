from transformers import pipeline
from PIL import Image

captioner = pipeline("image-to-text", model="nlpconnect/vit-gpt2-image-captioning")

image = Image.open("sample.jpg")

result = captioner(image)

print("Generated Caption:", result[0]['generated_text'])
