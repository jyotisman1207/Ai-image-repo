import cv2
import numpy as np

# Load image
img = cv2.imread("sample.jpg")

# Split channels
b, g, r = cv2.split(img)

# Find minimum channel value
dark_channel = np.minimum(np.minimum(r, g), b)

# Save result
cv2.imwrite("dark_channel.jpg", dark_channel)

print("Dark channel computed")
