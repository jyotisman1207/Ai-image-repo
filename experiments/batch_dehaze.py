import cv2
import numpy as np
import os

input_folder = "input_images"
output_folder = "outputs"

os.makedirs(output_folder, exist_ok=True)

for filename in os.listdir(input_folder):
    path = os.path.join(input_folder, filename)

    img = cv2.imread(path)
    if img is None:
        continue

    img = img.astype('float64') / 255

    dark = np.min(img, axis=2)
    A = np.max(dark)

    t = 1 - 0.95 * dark
    t = np.maximum(t, 0.1)

    J = (img - A) / t[:, :, None] + A
    J = np.clip(J, 0, 1)

    save_path = os.path.join(output_folder, filename)
    cv2.imwrite(save_path, J * 255)

print("Batch dehazing completed")
