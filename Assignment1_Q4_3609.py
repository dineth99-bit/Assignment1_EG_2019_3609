import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load the Lena image and convert it to grayscale
original_Image = cv2.imread('lena.png', cv2.IMREAD_GRAYSCALE)

# Check if the image is loaded successfully
if original_Image is None:
    print("Error: Image not loaded. Please check the file path.")
else:
    # Get the dimensions of the image
    height, width = original_Image.shape

    # Define arrays for downscaled images
    replaced_3X3 = np.zeros((height, width), dtype=np.uint8)
    replaced_5X5 = np.zeros((height, width), dtype=np.uint8)
    replaced_7X7 = np.zeros((height, width), dtype=np.uint8)

    # Define a function for averaging blocks of a given size
    def average(image, fact):
        for i in range(0, height, fact):
            for j in range(0, width, fact):
                block = original_Image[i:i+fact, j:j+fact]
                avg = np.mean(block)
                image[i:i+fact, j:j+fact] = avg

    # Averaging 3x3 block
    average(replaced_3X3, 3)

    # Averaging 5x5 block
    average(replaced_5X5, 5)

    # Averaging 7x7 block
    average(replaced_7X7, 7)

    # Plot the original and downscaled images
    fig, axs = plt.subplots(2, 2, figsize=(12, 9))
    axs[0, 0].imshow(original_Image, cmap='gray')
    axs[0, 0].set_title("Original Image")

    axs[0, 1].imshow(replaced_3X3, cmap='gray')
    axs[0, 1].set_title("Image downscaled by 3x3")

    axs[1, 0].imshow(replaced_5X5, cmap='gray')
    axs[1, 0].set_title("Image downscaled by 5x5")

    axs[1, 1].imshow(replaced_7X7, cmap='gray')
    axs[1, 1].set_title("Image downscaled by 7x7")

    plt.tight_layout()
    plt.show()
