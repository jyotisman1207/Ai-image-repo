import cv2
import numpy as np

# Load image
img = cv2.imread("sample.jpg")

# Convert to minimum channel
min_channel = np.min(img, axis=2)

# Apply minimum filter
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (15,15))
dark_channel = cv2.erode(min_channel, kernel)

# Save result
cv2.imwrite("dark_channel_patch.jpg", dark_channel)

print("Dark channel with patch computed")
