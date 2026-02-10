import cv2
import os
from pathlib import Path


def apply_canny_edge(image_path, threshold1=100, threshold2=150, output_folder=None):
    """    
    Args:
        image_path (str): Path to the input image file
        threshold1 (int): Lower threshold for Canny edge detection (default: 100)
        threshold2 (int): Upper threshold for Canny edge detection (default: 200)
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
        
        # Convert to grayscale first (required for Canny)
        grayscale_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        
        # Apply Canny edge detection
        edges = cv2.Canny(grayscale_image, threshold1, threshold2)
        
        # Create output folder if it doesn't exist
        os.makedirs(output_folder, exist_ok=True)
        
        # Get the filename from the input path
        filename = Path(image_path).stem
        file_ext = Path(image_path).suffix
        
        # Create output file path
        output_path = os.path.join(output_folder, f"{filename}_canny{file_ext}")
        
        # Save the processed image
        cv2.imwrite(output_path, edges)
        print(f"Canny edge detection applied and saved")        
        return True
    
    except Exception as e:
        print(f"Error: {str(e)}")
        return False
