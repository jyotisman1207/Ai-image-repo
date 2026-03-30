import cv2

# Load grayscale image
img = cv2.imread("sample.jpg", 0)

# Apply Otsu thresholding
_, otsu = cv2.threshold(
    img,
    0,
    255,
    cv2.THRESH_BINARY + cv2.THRESH_OTSU
)

# Save result
cv2.imwrite("otsu_threshold.jpg", otsu)

print("Otsu thresholding applied")
