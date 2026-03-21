import cv2
import numpy as np

# Load image
img = cv2.imread("sample.jpg").astype('float64') / 255

# Estimate dark channel
dark = np.min(img, axis=2)

# Estimate atmospheric light
A = np.max(dark)

# Estimate transmission
omega = 0.95
t = 1 - omega * dark

# Avoid division by zero
t = np.maximum(t, 0.1)

# Recover image
J = (img - A) / t[:, :, None] + A

# Clip values
J = np.clip(J, 0, 1)

# Save result
cv2.imwrite("dehazed_image.jpg", J * 255)

print("Dehazing completed")
