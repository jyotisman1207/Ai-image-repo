import cv2
import numpy as np

# Load image
img = cv2.imread("sample.jpg")

# Normalize
img = img / 255.0

# Gamma value
gamma = 2.0

# Apply gamma correction
corrected = np.power(img, gamma)

# Convert back
corrected = np.uint8(corrected * 255)

# Save result
cv2.imwrite("gamma_corrected.jpg", corrected)

print("Gamma correction applied")
