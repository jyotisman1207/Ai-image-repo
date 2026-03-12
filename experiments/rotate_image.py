from PIL import Image

# Load image
img = Image.open("sample.jpg")

# Rotate image by 90 degrees
rotated = img.rotate(90)

# Save rotated image
rotated.save("rotated_image.jpg")

print("Image rotation completed")
