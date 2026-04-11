from PIL import Image, ImageEnhance

img = Image.open("sample.jpg")

enhancer = ImageEnhance.Contrast(img)

contrast_img = enhancer.enhance(1.8)

contrast_img.save("contrast_image.jpg")

print("Contrast adjustment completed")
