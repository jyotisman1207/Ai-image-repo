import cv2
import numpy as np

# Load image
img = cv2.imread("sample.jpg")

# Normalize image
img = img / 255.0

# Estimate transmission map (basic)
omega = 0.95
dark_channel = np.min(img, axis=2)
transmission = 1 - omega * dark_channel

# Save result
cv2.imwrite("transmission_map.jpg", transmission * 255)

print("Transmission map computed")
