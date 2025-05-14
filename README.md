# Grayscale Pixel Editor in Google Colab

This repository contains a Python script that allows users to interactively modify either a single pixel or a block of pixels in a grayscale image using OpenCV and NumPy. The program is designed to run in **Google Colab** and supports image upload, grayscale conversion, pixel/block editing, and real-time image display.

---

## 👨‍🏫 Developer
**Samie Tahir**  
Course: *Computer Vision*

---

## 📚 Features

- Upload any image using Google Colab file uploader
- Convert the image to grayscale
- View a 20x20 block of the grayscale matrix
- Modify a **single pixel** or a **block of pixels** in the grayscale image
- Display original and modified images using `cv2_imshow`

---

## 🛠️ Libraries Used

- `opencv-python-headless` (`cv2`) – For image reading, processing, and displaying
- `numpy` – For handling the image matrix and operations
- `google.colab` – For uploading files and displaying images in Colab

---

## ▶️ How to Run

1. Open the script in [Google Colab](https://colab.research.google.com/).
2. Run all cells to:
   - Install required libraries
   - Upload your image
   - Convert it to grayscale
   - Modify pixels interactively
3. Choose between modifying a single pixel or a block.
4. View the updated grayscale image at the end.



## 📄 License

This project is shared for educational purposes. You may use, modify, and share it freely with proper credit.
