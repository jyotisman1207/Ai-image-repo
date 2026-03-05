from PIL import Image

# Load image
img = Image.open("sample.jpg")

# Resize image
resized = img.resize((256, 256))

# Convert to grayscale
gray = img.convert("L")

# Save processed images
resized.save("resized_image.jpg")
gray.save("grayscale_image.jpg")

print("Image preprocessing completed")
