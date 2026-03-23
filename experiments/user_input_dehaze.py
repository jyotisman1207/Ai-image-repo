import cv2
import numpy as np

# Take input from user
image_path = input("Enter image path: ")

# Load image
img = cv2.imread(image_path).astype('float64') / 255

# Dark channel
dark = np.min(img, axis=2)

# Atmospheric light
A = np.max(dark)

# Transmission
omega = 0.95
t = 1 - omega * dark
t = np.maximum(t, 0.1)

# Recover image
J = (img - A) / t[:, :, None] + A
J = np.clip(J, 0, 1)

# Save output
cv2.imwrite("output.jpg", J * 255)

print("Dehazed image saved as output.jpg")
