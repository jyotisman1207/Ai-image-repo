import cv2
import numpy as np

# Load image in grayscale
img = cv2.imread("sample.jpg", 0)

# Sobel X and Y
sobelx = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=3)
sobely = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=3)

# Magnitude
magnitude = cv2.magnitude(sobelx, sobely)
magnitude = np.uint8(np.clip(magnitude, 0, 255))

# Save
cv2.imwrite("sobel_edges.jpg", magnitude)

print("Sobel edge detection completed")
