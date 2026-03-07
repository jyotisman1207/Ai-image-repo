from PIL import Image, ImageEnhance

# Load image
img = Image.open("sample.jpg")

# Create brightness enhancer
enhancer = ImageEnhance.Brightness(img)

# Increase brightness
bright_img = enhancer.enhance(1.5)

# Save result
bright_img.save("bright_image.jpg")

print("Brightness adjustment completed")
