import cv2
import numpy as np

# Load grayscale image
img = cv2.imread("sample.jpg", 0)

# Apply Laplacian
laplacian = cv2.Laplacian(img, cv2.CV_64F)
laplacian = np.uint8(np.absolute(laplacian))

# Save result
cv2.imwrite("laplacian_edges.jpg", laplacian)

print("Laplacian edge detection applied")
