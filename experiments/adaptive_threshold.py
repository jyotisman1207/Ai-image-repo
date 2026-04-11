import cv2

img = cv2.imread("sample.jpg", 0)

thresh = cv2.adaptiveThreshold(
    img,
    255,
    cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
    cv2.THRESH_BINARY,
    11,
    2
)

cv2.imwrite("adaptive_threshold.jpg", thresh)

print("Adaptive threshold applied")
