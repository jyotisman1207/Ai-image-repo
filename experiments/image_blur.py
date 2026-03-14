import cv2

# Load image
img = cv2.imread("sample.jpg")

# Apply blur
blur = cv2.blur(img, (7,7))

# Save result
cv2.imwrite("blur_image.jpg", blur)

print("Image blur applied")
