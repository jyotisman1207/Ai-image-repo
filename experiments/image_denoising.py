import cv2

# Load image
img = cv2.imread("sample.jpg")

# Apply Gaussian Blur to remove noise
denoised = cv2.GaussianBlur(img, (5, 5), 0)

# Save result
cv2.imwrite("denoised_image.jpg", denoised)

print("Image denoising completed")
