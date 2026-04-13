import cv2
import numpy as np

image_path = input("Enter image path: ")

img = cv2.imread(image_path).astype('float64') / 255

dark = np.min(img, axis=2)
A = np.max(dark)

omega = 0.95
t = 1 - omega * dark
t = np.maximum(t, 0.1)


J = (img - A) / t[:, :, None] + A
J = np.clip(J, 0, 1)

cv2.imwrite("output.jpg", J * 255)

print("Dehazed image saved as output.jpg")
