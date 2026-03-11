from PIL import Image

# Load image
img = Image.open("sample.jpg")

# Flip horizontally
flipped = img.transpose(Image.FLIP_LEFT_RIGHT)

# Save result
flipped.save("flipped_image.jpg")

print("Image flipped successfully")
