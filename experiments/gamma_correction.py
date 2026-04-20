import cv2
import numpy as np

img = cv2.imread("sample.jpg")

img = img / 255.0

gamma = 2.0

corrected = np.power(img, gamma)

corrected = np.uint8(corrected * 255)

cv2.imwrite("gamma_corrected.jpg", corrected)

print("Gamma correction applied")
