from PIL import Image

img = Image.open("sample.jpg")
resized = img.resize((256, 256))

gray = img.convert("L")

resized.save("resized_image.jpg")
gray.save("grayscale_image.jpg")

print("Image preprocessing completed")
