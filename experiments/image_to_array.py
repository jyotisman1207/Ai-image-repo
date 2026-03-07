from PIL import Image
import numpy as np


img = Image.open("sample.jpg")

img_array = np.array(img)

print("Array shape:", img_array.shape)
print("Height:", img_array.shape[0])
print("Width:", img_array.shape[1])
print("Channels (RGB):", img_array.shape[2])
