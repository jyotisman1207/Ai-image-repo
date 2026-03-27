import cv2
import numpy as np

# Load image in grayscale
img = cv2.imread("sample.jpg", 0)

# Kernel
kernel = np.ones((5,5), np.uint8)

# Erosion
erosion = cv2.erode(img, kernel, iterations=1)

# Dilation
dilation = cv2.dilate(img, kernel, iterations=1)

# Save outputs
cv2.imwrite("erosion.jpg", erosion)
cv2.imwrite("dilation.jpg", dilation)

print("Morphological operations applied")
