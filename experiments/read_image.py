from PIL import Image

img = Image.open("133915006288739743.jpg")

print("Image format:", img.format)
print("Image size (width, height):", img.size)
print("Color mode:", img.mode)


width, height = img.size
print("Total pixels:", width * height)
