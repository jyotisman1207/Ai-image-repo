import cv2
import numpy as np

img = cv2.imread("sample.jpg")

img = img / 255.0

omega = 0.95
dark_channel = np.min(img, axis=2)
transmission = 1 - omega * dark_channel

cv2.imwrite("transmission_map.jpg", transmission * 255)

print("Transmission map computed")
