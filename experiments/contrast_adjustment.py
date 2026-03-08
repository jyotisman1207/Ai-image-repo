from PIL import Image, ImageEnhance

# Load image
img = Image.open("sample.jpg")

# Create contrast enhancer
enhancer = ImageEnhance.Contrast(img)

# Increase contrast
contrast_img = enhancer.enhance(1.8)

# Save result
contrast_img.save("contrast_image.jpg")

print("Contrast adjustment completed")
