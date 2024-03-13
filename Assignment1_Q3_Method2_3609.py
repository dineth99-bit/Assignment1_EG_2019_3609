import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load the image and convert it to RGB color space
original_img = cv2.cvtColor(cv2.imread('Resources/lena.png'), cv2.COLOR_BGR2RGB)

# Extracting the height and width of the image
image_height, image_width = original_img.shape[:2]

# Define the center point of the image
center = (image_width / 2, image_height / 2)

# Generate rotation matrices for 45 and 90 degrees
rotation_matrix_45_deg = cv2.getRotationMatrix2D(center, 45, 1)
rotation_matrix_90_deg = cv2.getRotationMatrix2D(center, 90, 1)

# Adjust the size of the rotated image for a 45-degree rotation
new_dimension = int((image_height + image_width) / np.sqrt(2))
rotation_matrix_45_deg[0, 2] += (new_dimension / 2) - center[0]
rotation_matrix_45_deg[1, 2] += (new_dimension / 2) - center[1]

# Adjust the size of the rotated image for a 90-degree rotation
rotation_matrix_90_deg[0, 2] += (image_height / 2) - center[0]
rotation_matrix_90_deg[1, 2] += (image_width / 2) - center[1]

# Apply rotation to the image without cropping the corners
rotated_img_45_deg = cv2.warpAffine(original_img, rotation_matrix_45_deg, (new_dimension, new_dimension), flags=cv2.INTER_LINEAR)
rotated_img_90_deg = cv2.warpAffine(original_img, rotation_matrix_90_deg, (image_height, image_width), flags=cv2.INTER_LINEAR)

# Plot the results
fig, (axis1, axis2) = plt.subplots(1, 2, figsize=(12, 6))

# Display the image rotated by 45 degrees
axis1.imshow(rotated_img_45_deg)
axis1.set_title("Image rotated by 45 degrees\n")

# Display the image rotated by 90 degrees
axis2.imshow(rotated_img_90_deg)
axis2.set_title("Image rotated by 90 degrees\n")

plt.show()
