import cv2
import numpy as np


img = cv2.imread("sample.jpg")


b, g, r = cv2.split(img)


dark_channel = np.minimum(np.minimum(r, g), b)


cv2.imwrite("dark_channel.jpg", dark_channel)

print("Dark channel computed")
