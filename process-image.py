from module.median_blur import apply_median_blur
from module.grayscale import apply_grayscale
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



if __name__ == "__main__":
    process_images()

