import cv2
import os
import numpy as np
from pathlib import Path

def apply_five_filters(image_path, output_folder=None):   
    # Applies all five filters sequentially to the input image and saves the final combined result.
    
    # Read the original image
    image = cv2.imread(image_path)

    # Apply filters
    emboss_kernel = np.array([[-2, -1, 0],
                              [-1,  1, 1],
                              [ 0,  1, 2]], dtype=np.float32)
    filtered_image = cv2.filter2D(image.astype(np.float32), -1, emboss_kernel).astype(np.uint8) #Emboss filter
    filtered_image = cv2.bilateralFilter(filtered_image, 9, 75, 75) #Bilateral filter (diameter=9, sigmaColor=75, sigmaSpace=75)
    filtered_image = cv2.cvtColor(filtered_image, cv2.COLOR_BGR2GRAY) #Grayscale conversion
    filtered_image = cv2.medianBlur(filtered_image, 5) #Median blur (kernel_size=5)
    filtered_image = cv2.Canny(filtered_image, 100, 150) #Canny edge detection

    # Save the combined result
    filename = Path(image_path).stem
    file_ext = Path(image_path).suffix
    output_path = os.path.join(output_folder, f"{filename}_FiveFilters{file_ext}")
    cv2.imwrite(output_path, filtered_image)
    print(f"Combined five filters applied to {filename}")


def apply_four_filters(image_path, output_folder=None):   
    # Applies four filters sequentially to the input image and saves the final combined result.
    
    # Read the original image
    image = cv2.imread(image_path)

    # Apply filters
    filtered_image = cv2.medianBlur(image, 5) #Median blur (kernel_size=5)
    emboss_kernel = np.array([[-2, -1, 0],
                              [-1,  1, 1],
                              [ 0,  1, 2]], dtype=np.float32)
    filtered_image = cv2.filter2D(filtered_image.astype(np.float32), -1, emboss_kernel).astype(np.uint8) #Emboss filter
    filtered_image = cv2.bilateralFilter(filtered_image, 9, 75, 75) #Bilateral filter (diameter=9, sigmaColor=75, sigmaSpace=75)
    filtered_image = cv2.cvtColor(filtered_image, cv2.COLOR_BGR2GRAY) #Grayscale conversion
    

    # Save the combined result
    filename = Path(image_path).stem
    file_ext = Path(image_path).suffix
    output_path = os.path.join(output_folder, f"{filename}_FourFilters{file_ext}")
    cv2.imwrite(output_path, filtered_image)
    print(f"Combined four filters applied to {filename}")