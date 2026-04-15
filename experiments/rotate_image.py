from PIL import Image

img = Image.open("sample.jpg")

rotated = img.rotate(90)

rotated.save("rotated_image.jpg")

print("Image rotation completed")
