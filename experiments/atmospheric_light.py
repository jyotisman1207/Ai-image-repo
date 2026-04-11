import cv2
import numpy as np


img = cv2.imread("sample.jpg")

dark = np.min(img, axis=2)

A = np.max(dark)

print("Estimated atmospheric light:", A)
