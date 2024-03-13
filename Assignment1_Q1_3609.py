import cv2
import numpy as np
import matplotlib.pyplot as plt

def reduce_intensity_levels(image, levels):

    # Find the maximum intensity value in the image
    max_intensity = np.max(image)

    # Calculate the factor by which intensity levels need to be reduced
    factor = 255 / (levels - 1)

    # Quantize the image by rounding pixel values to the nearest level
    quantized_image = np.round(image / factor) * factor

    # Clip pixel values to ensure they are within the valid range for np.uint8
    quantized_image = np.clip(quantized_image, 0, 255)

    # Convert the quantized image to uint8 data type (required for image display)
    return np.uint8(quantized_image)

# using the lean.png image since due to its balance of diverse features, moderate complexity, and historical significance.
# Load the image


image = cv2.imread("lena.png", cv2.IMREAD_GRAYSCALE)

# Prompt the user to input the desired number of intensity levels
while True:
    try:
        desired_levels = int(input("Please enter the required number of intensity levels from 1 to 8: "))
        if 1 <= desired_levels <= 8:
            break
        else:
            print("The value should be between 1 and 8")
    except ValueError:
        print("Invalid input")

# Reduce intensity levels using the function defined above
modified_image = reduce_intensity_levels(image, 2 ** desired_levels)

# Plot the original and modified images using matplotlib
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.imshow(image, cmap='gray')
plt.title("Original Image")
plt.axis('on')

plt.subplot(1, 2, 2)
plt.imshow(modified_image, cmap='gray')
plt.title("Modified Image ({} intensity levels)".format(2 ** desired_levels))
plt.axis('on')

plt.show()
