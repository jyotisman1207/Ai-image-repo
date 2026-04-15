import cv2
import numpy as np

img = cv2.imread("sample.jpg", 0)

sobelx = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=3)
sobely = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=3)
magnitude = cv2.magnitude(sobelx, sobely)
magnitude = np.uint8(np.clip(magnitude, 0, 255))


cv2.imwrite("sobel_edges.jpg", magnitude)

print("Sobel edge detection completed")
