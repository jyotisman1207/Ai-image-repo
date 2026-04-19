from PIL import Image
import numpy as np
import matplotlib.pyplot as plt


img = Image.open("sample.jpg")


gray = img.convert("L")

img_array = np.array(gray)

plt.hist(img_array.flatten(), bins=256, range=[0,256])
plt.title("Image Histogram")
plt.xlabel("Pixel Intensity")
plt.ylabel("Frequency")

plt.show()
