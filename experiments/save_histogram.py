import cv2
import matplotlib.pyplot as plt

# Load grayscale image
img = cv2.imread("sample.jpg", 0)

# Plot histogram
plt.hist(img.ravel(), bins=256, range=[0,256])
plt.title("Histogram")
plt.xlabel("Pixel Intensity")
plt.ylabel("Frequency")

# Save histogram image
plt.savefig("histogram.png")
plt.close()

print("Histogram saved as image")
