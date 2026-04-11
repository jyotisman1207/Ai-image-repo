from PIL import Image, ImageEnhance

img = Image.open("sample.jpg")

enhancer = ImageEnhance.Brightness(img)

bright_img = enhancer.enhance(1.5)

bright_img.save("bright_image.jpg")

print("Brightness adjustment completed")
