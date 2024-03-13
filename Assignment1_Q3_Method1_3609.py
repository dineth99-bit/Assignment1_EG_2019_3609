import cv2
import matplotlib.pyplot as plt

# Load the image
image = cv2.imread('lena.png')

# Rotate by 45 degrees
rows, cols = image.shape[:2]
rotation_matrix_45 = cv2.getRotationMatrix2D((cols/2, rows/2), 45, 1)
rotated_image_45 = cv2.warpAffine(image, rotation_matrix_45, (cols, rows))

# Rotate by 90 degrees
rotation_matrix_90 = cv2.getRotationMatrix2D((cols/2, rows/2), 90, 1)
rotated_image_90 = cv2.warpAffine(image, rotation_matrix_90, (cols, rows))

# Plot the images
plt.figure(figsize=(10, 5))

plt.subplot(1, 3, 1)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title('Original Image')
plt.xlabel('X')
plt.ylabel('Y')

plt.subplot(1, 3, 2)
plt.imshow(cv2.cvtColor(rotated_image_45, cv2.COLOR_BGR2RGB))
plt.title('Rotated by 45 degrees')
plt.xlabel('X')
plt.ylabel('Y')

plt.subplot(1, 3, 3)
plt.imshow(cv2.cvtColor(rotated_image_90, cv2.COLOR_BGR2RGB))
plt.title('Rotated by 90 degrees')
plt.xlabel('X')
plt.ylabel('Y')

plt.tight_layout()
plt.show()
