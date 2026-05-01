from PIL import Image
import numpy as np
import cv2

img = cv2.imread("sample.jpg")

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

equalized = cv2.equalizeHist(gray)

cv2.imwrite("equalized_image.jpg", equalized)

print("Histogram equalization applied")
