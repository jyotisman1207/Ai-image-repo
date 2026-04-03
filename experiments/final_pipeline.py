import cv2
import numpy as np
from transformers import pipeline
from PIL import Image

# Load caption model
captioner = pipeline("image-to-text", model="nlpconnect/vit-gpt2-image-captioning")

# Take input
image_path = input("Enter image path: ")

# Load image
img = cv2.imread(image_path)

if img is None:
    print("Error loading image")
    exit()

# Normalize
img_float = img.astype('float64') / 255

# Dark channel
dark = np.min(img_float, axis=2)

# Atmospheric light
A = np.max(dark)

# Transmission
t = 1 - 0.95 * dark
t = np.maximum(t, 0.1)

# Recover image
J = (img_float - A) / t[:, :, None] + A
J = np.clip(J, 0, 1)

# Save dehazed image
cv2.imwrite("final_dehazed.jpg", J * 255)

# Convert to PIL for captioning
pil_image = Image.fromarray((J * 255).astype('uint8'))

# Generate caption
result = captioner(pil_image)
caption = result[0]['generated_text']

# Save caption
with open("final_caption.txt", "w") as f:
    f.write(caption)

print("Dehazing + Caption completed")
print("Caption:", caption)
