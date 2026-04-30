import cv2

img = cv2.imread("sample.jpg")

blur = cv2.blur(img, (7,7))

cv2.imwrite("blur_image.jpg", blur)

print("Image blur applied")
