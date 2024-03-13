import cv2
import numpy as np
import matplotlib.pyplot as plt

# using the lean.png image since due to its balance of diverse features, moderate complexity, and historical significance.
# Load the image
image = cv2.imread("lena.png", cv2.IMREAD_GRAYSCALE)

# Function to perform spatial averaging
def spatial_average(image, kernel_size):
    # Define the kernel
    kernel = np.ones((kernel_size, kernel_size), np.float32) / (kernel_size * kernel_size)
    # Apply the filter
    averaged = cv2.filter2D(image, -1, kernel)
    return averaged

# Perform spatial averaging for 3x3 neighborhood
averaged_3x3 = spatial_average(image, 3)

# Perform spatial averaging for 10x10 neighborhood
averaged_10x10 = spatial_average(image, 10)

# Perform spatial averaging for 20x20 neighborhood
averaged_20x20 = spatial_average(image, 20)

# Display the original and averaged images using matplotlib
plt.figure(figsize=(12, 8))

plt.subplot(2, 2, 1)
plt.imshow(image, cmap='gray')
plt.title('Original')

plt.subplot(2, 2, 2)
plt.imshow(averaged_3x3, cmap='gray')
plt.title('3x3 Averaged')

plt.subplot(2, 2, 3)
plt.imshow(averaged_10x10, cmap='gray')
plt.title('10x10 Averaged')

plt.subplot(2, 2, 4)
plt.imshow(averaged_20x20, cmap='gray')
plt.title('20x20 Averaged')

plt.show()
