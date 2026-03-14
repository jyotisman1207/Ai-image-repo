import cv2

# Load image
img = cv2.imread("sample.jpg", 0)

# Apply threshold
_, binary = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)

# Save result
cv2.imwrite("binary_image.jpg", binary)

print("Binary threshold applied")
