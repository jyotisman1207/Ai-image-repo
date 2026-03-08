from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

# Load image
img = Image.open("sample.jpg")

# Convert to grayscale
gray = img.convert("L")

# Convert to numpy array
img_array = np.array(gray)

# Plot histogram
plt.hist(img_array.flatten(), bins=256, range=[0,256])
plt.title("Image Histogram")
plt.xlabel("Pixel Intensity")
plt.ylabel("Frequency")

plt.show()
