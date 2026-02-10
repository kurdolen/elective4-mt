import cv2
import os
from pathlib import Path


def apply_median_blur(image_path, output_folder=None, kernel_size=5):
    """    
    Args:
        image_path (str): Path to the input image file
        output_folder (str): Path to the folder where the processed image will be saved (default: ../output)
        kernel_size (int): Size of the median filter kernel (must be odd, default: 5)
    
    Returns:
        bool: True if successful, False otherwise
    """
    try:
        # If output_folder not specified, use the project's output folder
        if output_folder is None:
            module_dir = Path(__file__).parent
            output_folder = str(module_dir.parent / "output")
        
        # Read the image
        image = cv2.imread(image_path)
        
        if image is None:
            print(f"Error: Could not find image from {image_path}")
            return False
        
        # Ensure kernel size is odd
        if kernel_size % 2 == 0:
            kernel_size += 1
        
        # Apply median blur
        blurred_image = cv2.medianBlur(image, kernel_size)
        
        # Create output folder if it doesn't exist
        os.makedirs(output_folder, exist_ok=True)
        
        # Get the filename from the input path
        filename = Path(image_path).stem
        file_ext = Path(image_path).suffix
        
        # Create output file path
        output_path = os.path.join(output_folder, f"{filename}_median_blur{file_ext}")
        
        # Save the processed image
        cv2.imwrite(output_path, blurred_image)
        print(f"Median blur applied and saved")
        return True
    
    except Exception as e:
        print(f"Error: {str(e)}")
        return False


