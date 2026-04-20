from PIL import Image


img = Image.open("sample.jpg")

flipped = img.transpose(Image.FLIP_LEFT_RIGHT)

flipped.save("flipped_image.jpg")

print("Image flipped successfully")
