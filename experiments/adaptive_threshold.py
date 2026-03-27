import cv2

# Load image in grayscale
img = cv2.imread("sample.jpg", 0)

# Apply adaptive threshold
thresh = cv2.adaptiveThreshold(
    img,
    255,
    cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
    cv2.THRESH_BINARY,
    11,
    2
)

# Save result
cv2.imwrite("adaptive_threshold.jpg", thresh)

print("Adaptive threshold applied")
