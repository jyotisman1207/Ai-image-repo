import cv2

img = cv2.imread("sample.jpg")

hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

cv2.imwrite("hsv_image.jpg", hsv)

print("Converted to HSV color space")
