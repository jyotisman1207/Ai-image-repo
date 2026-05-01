import cv2

img = cv2.imread("sample.jpg")

denoised = cv2.GaussianBlur(img, (5, 5), 0)

cv2.imwrite("denoised_image.jpg", denoised)

print("Image denoising completed")
