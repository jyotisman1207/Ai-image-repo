from PIL import Image

img = Image.open("sample.jpg")

print("Image format:", img.format)
print("Image size (width, height):", img.size)
print("Color mode:", img.mode)


width, height = img.size
print("Total pixels:", width * height)
