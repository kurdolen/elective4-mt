from module.median_blur import apply_median_blur
from module.grayscale import apply_grayscale
from module.canny_edge import apply_canny_edge
from module.emboss_filter import apply_emboss_filter
from module.bilateral_filter import apply_bilateral_filter
from module.combine_filters import apply_five_filters, apply_four_filters
import cv2
import os
from pathlib import Path

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
INPUT_DIR = os.path.join(BASE_DIR, "input")
OUTPUT_DIR = os.path.join(BASE_DIR, "output")

def process_image():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    
    for filename in os.listdir(INPUT_DIR):
        if not filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.tiff')):
            continue
        image_path = os.path.join(INPUT_DIR, filename)
        print(f"\nProcessing {filename}...")
        
        # Apply filters individually
        apply_median_blur(image_path, output_folder=OUTPUT_DIR)
        apply_grayscale(image_path, output_folder=OUTPUT_DIR)
        apply_canny_edge(image_path, output_folder=OUTPUT_DIR)
        apply_emboss_filter(image_path, output_folder=OUTPUT_DIR)
        apply_bilateral_filter(image_path, output_folder=OUTPUT_DIR)
        
        # Apply all filters sequentially for combined result
        apply_five_filters(image_path, OUTPUT_DIR)
        apply_four_filters(image_path, OUTPUT_DIR)

if __name__ == "__main__":
    process_image()

