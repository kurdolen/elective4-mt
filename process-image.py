from module.median_blur import apply_median_blur
from module.grayscale import apply_grayscale
from module.canny_edge import apply_canny_edge
from module.emboss_filter import apply_emboss_filter
from module.bilateral_filter import apply_bilateral_filter
from pathlib import Path
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
INPUT_DIR = os.path.join(BASE_DIR, "input")
OUTPUT_DIR = os.path.join(BASE_DIR, "output")

def process_images():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    
    for filename in os.listdir(INPUT_DIR):
        if not filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.tiff')):
            continue
        image_path = os.path.join(INPUT_DIR, filename)
        print(f"Processing {image_path}...")
        
        # Apply median blur
        if apply_median_blur(image_path, output_folder=OUTPUT_DIR):
            print(f"Median blur applied successfully for {filename}")
        else:
            print(f"Failed to apply median blur for {filename}")
        
        # Apply grayscale conversion
        if apply_grayscale(image_path, output_folder=OUTPUT_DIR):
            print(f"Grayscale conversion applied successfully for {filename}")
        else:
            print(f"Failed to apply grayscale conversion for {filename}")

        # Apply Canny edge detection
        if apply_canny_edge(image_path, output_folder=OUTPUT_DIR):
            print(f"Canny edge detection applied successfully for {filename}")
        else:
            print(f"Failed to apply Canny edge detection for {filename}")
            
        # Apply emboss filter
        if apply_emboss_filter(image_path, output_folder=OUTPUT_DIR):
            print(f"Emboss filter applied successfully for {filename}")
        else:
            print(f"Failed to apply emboss filter for {filename}")
            
        # Apply bilateral filter
        if apply_bilateral_filter(image_path, output_folder=OUTPUT_DIR):
            print(f"Bilateral filter applied successfully for {filename}")
        else:
            print(f"Failed to apply bilateral filter for {filename}")

if __name__ == "__main__":
    process_images()

