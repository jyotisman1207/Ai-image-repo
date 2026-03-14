import cv2
import numpy as np

# Load image
img = cv2.imread("sample.jpg")

# Sharpening kernel
kernel = np.array([[0,-1,0],
                   [-1,5,-1],
                   [0,-1,0]])

# Apply sharpening
sharpened = cv2.filter2D(img, -1, kernel)

# Save result
cv2.imwrite("sharpened_image.jpg", sharpened)

print("Image sharpening applied")
