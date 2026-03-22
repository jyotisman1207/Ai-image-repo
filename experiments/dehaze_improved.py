import cv2
import numpy as np

# Load image
img = cv2.imread("sample.jpg").astype('float64') / 255

# Dark channel
dark = np.min(img, axis=2)

# Atmospheric light
A = np.max(dark)

# Transmission map
omega = 0.95
t = 1 - omega * dark

# Smooth transmission using Gaussian blur
t = cv2.GaussianBlur(t, (15,15), 0)

# Avoid very small values
t = np.maximum(t, 0.1)

# Recover image
J = (img - A) / t[:, :, None] + A

# Clip values
J = np.clip(J, 0, 1)

# Save result
cv2.imwrite("dehazed_improved.jpg", J * 255)

print("Improved dehazing completed")
