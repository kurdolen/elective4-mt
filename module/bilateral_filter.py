import cv2
import os
from pathlib import Path


def apply_bilateral_filter(image_path, diameter=9, sigma_color=75, sigma_space=75, output_folder=None):
    """    
    Args:
        image_path (str): Path to the input image file
        diameter (int): Diameter of each pixel neighborhood (default: 9)
        sigma_color (int): Filter sigma in the color space (default: 75)
        sigma_space (int): Filter sigma in the coordinate space (default: 75)
        output_folder (str): Path to the folder where the processed image will be saved (default: ../output)
    
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
        
        # Apply bilateral filter
        filtered_image = cv2.bilateralFilter(image, diameter, sigma_color, sigma_space)
        
        # Create output folder if it doesn't exist
        os.makedirs(output_folder, exist_ok=True)
        
        # Get the filename from the input path
        filename = Path(image_path).stem
        file_ext = Path(image_path).suffix
        
        # Create output file path
        output_path = os.path.join(output_folder, f"{filename}_bilateral{file_ext}")
        
        # Save the processed image
        cv2.imwrite(output_path, filtered_image)
        print(f"Bilateral filter applied and saved")        
        return True
    
    except Exception as e:
        print(f"Error: {str(e)}")
        return False
