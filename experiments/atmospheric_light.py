import cv2
import numpy as np

# Load image
img = cv2.imread("sample.jpg")

# Compute dark channel
dark = np.min(img, axis=2)

# Estimate atmospheric lightnsjsn
A = np.max(dark)

print("Estimated atmospheric light:", A)
