import cv2

# Load image
img = cv2.imread("sample.jpg")

# Convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Detect edges
edges = cv2.Canny(gray, 100, 200)

# Save result
cv2.imwrite("edges_image.jpg", edges)

print("Edge detection completed")
