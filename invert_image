from PIL import Image
import numpy as np

# Load image
img = Image.open("sample.jpg")

# Convert image to numpy array
img_array = np.array(img)

# Invert colors
inverted_array = 255 - img_array

# Convert back to image
inverted_img = Image.fromarray(inverted_array)

# Save result
inverted_img.save("inverted_image.jpg")

print("Image inversion completed")
