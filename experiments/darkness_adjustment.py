from PIL import Image, ImageEnhance


img = Image.open("sample.jpg")


enhancer = ImageEnhance.Brightness(img)


dark_img = enhancer.enhance(0.5)

dark_img.save("dark_image.jpg")

print("Darkness adjustment completed")
