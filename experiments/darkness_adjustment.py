from PIL import Image, ImageEnhance

# Load image
img = Image.open("sample.jpg")

# Create brightness controller
enhancer = ImageEnhance.Brightness(img)

# Reduce brightness
dark_img = enhancer.enhance(0.5)

# Save result
dark_img.save("dark_image.jpg")

print("Darkness adjustment completed")
