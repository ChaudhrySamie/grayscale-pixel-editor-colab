#Developed By; Samie Tahir
# With assistance from Google search and ChatGPT (OpenAI)

!pip install opencv-python-headless

import cv2
import numpy as np
from google.colab import files
from google.colab.patches import cv2_imshow

uploaded = files.upload()
image_path = list(uploaded.keys())[0]

original_image = cv2.imread(image_path)
gray_image = cv2.cvtColor(original_image, cv2.COLOR_BGR2GRAY)

print("Original Image (Color):")
cv2_imshow(original_image)

print("Grayscale Image Matrix (20x20 block):")
print(gray_image[:20, :20])

while True:
    choice = input("Do you want to modify a single pixel (p) or a block of pixels (b)? (p/b): ").lower()

    if choice == 'p':
        try:
            row = int(input(f"\nEnter row number (0 to {gray_image.shape[0]-1}): "))
            col = int(input(f"Enter column number (0 to {gray_image.shape[1]-1}): "))
            new_value = int(input("Enter new pixel value (0-255): "))

            if 0 <= row < gray_image.shape[0] and 0 <= col < gray_image.shape[1]:
                gray_image[row, col] = new_value
                print(f"Modified pixel at ({row},{col}) with value {new_value}")
            else:
                print("Error: The pixel position is out of bounds!")

        except Exception as e:
            print("Invalid input:", e)

    elif choice == 'b':
        try:
            row_start = int(input(f"\nEnter starting row (0 to {gray_image.shape[0]-1}): "))
            col_start = int(input(f"Enter starting column (0 to {gray_image.shape[1]-1}): "))
            block_height = int(input("Enter block height: "))
            block_width = int(input("Enter block width: "))
            new_value = int(input("Enter new pixel value (0-255): "))

            row_end = min(row_start + block_height, gray_image.shape[0])
            col_end = min(col_start + block_width, gray_image.shape[1])

            gray_image[row_start:row_end, col_start:col_end] = new_value
            print(f"Modified block from ({row_start},{col_start}) to ({row_end},{col_end}) with value {new_value}")

        except Exception as e:
            print("Invalid input:", e)

    else:
        print("Invalid choice. Please enter 'p' for pixel or 'b' for block.")

    cont = input("Do you want to modify another pixel or block? (yes/no): ").lower()
    if cont != "yes":
        break

print("Modified Grayscale Image:")
cv2_imshow(gray_image)
