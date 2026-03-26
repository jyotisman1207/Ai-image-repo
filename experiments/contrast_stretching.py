import cv2
import numpy as np

# Load image in grayscale
img = cv2.imread("sample.jpg", 0)

# Find min and max pixel values
min_val = np.min(img)
max_val = np.max(img)

# Apply contrast stretching
stretched = (img - min_val) * (255 / (max_val - min_val))

# Convert to uint8
stretched = np.uint8(stretched)

# Save result
cv2.imwrite("contrast_stretched.jpg", stretched)

print("Contrast stretching completed")
