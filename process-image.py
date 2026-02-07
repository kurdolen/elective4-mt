from module.median_blur import apply_median_blur
from pathlib import Path
import os
from PIL import Image

# Input and output folder paths
input_folder = Path("input")
output_folder = Path("output")

def process_images():
    # Process all images in the input folder
    for image_file in input_folder.glob("*"):
        if image_file.is_file() and image_file.suffix.lower() in [".jpg", ".jpeg", ".png", ".bmp"]:
            img = Image.open(image_file)
            blurred_img = apply_median_blur(img)
            output_path = output_folder / image_file.name
            blurred_img.save(output_path)
            print(f"Processed: {image_file.name}")

if __name__ == "__main__":
    process_images()
