import os
import pytest
import shutil
import process_image  

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
INPUT_DIR = os.path.join(BASE_DIR, "input")
OUTPUT_DIR = os.path.join(BASE_DIR, "output")

def test_input_folder_has_images():
    """
    Verifies that you actually have images in your input folder to test.
    """
    assert os.path.exists(INPUT_DIR), f"Input directory does not exist at {INPUT_DIR}"
    
    files = os.listdir(INPUT_DIR)
    image_files = [f for f in files if f.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.tiff'))]
    
    assert len(image_files) > 0, "No image files found in the input directory! Please add some images."
    print(f"\nFound {len(image_files)} images to process: {image_files}")

def test_process_real_images():
    """
    Runs the REAL process_images() function on your specific input files.
    Then checks if the output folder contains processed results.
    """

    print("\nRunning image processing pipeline on real files...")
    process_image.process_images()
    
    assert os.path.exists(OUTPUT_DIR), "Output directory was not created."
    
    input_files = [f for f in os.listdir(INPUT_DIR) if f.lower().endswith(('.png', '.jpg', '.jpeg'))]
    output_files = os.listdir(OUTPUT_DIR)
    
    assert len(output_files) > 0, "The processing finished, but the output folder is empty."
    
    expected_min_files = len(input_files)
    assert len(output_files) >= expected_min_files, \
        f"Expected at least {expected_min_files} output files, but found {len(output_files)}."
        
    print(f"\nSuccess! Processed {len(input_files)} input images into {len(output_files)} output files.")