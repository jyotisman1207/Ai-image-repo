from PIL import Image
import numpy as np
import cv2

# Load image
img = cv2.imread("sample.jpg")

# Convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Apply histogram equalization
equalized = cv2.equalizeHist(gray)

# Save result
cv2.imwrite("equalized_image.jpg", equalized)

print("Histogram equalization applied")
