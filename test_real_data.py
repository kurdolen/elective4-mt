import os
import pytest
import shutil
import process_image  # Import your main script

# --- Configuration ---
# These point to your ACTUAL folders
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
    # 1. (Optional) Clear the output folder first so we know results are fresh
    # Uncomment the next two lines if you want to wipe the output folder before every test
    # if os.path.exists(OUTPUT_DIR):
    #     shutil.rmtree(OUTPUT_DIR)
    
    # 2. Run the actual application logic
    print("\nRunning image processing pipeline on real files...")
    process_image.process_images()
    
    # 3. Verify Output
    assert os.path.exists(OUTPUT_DIR), "Output directory was not created."
    
    input_files = [f for f in os.listdir(INPUT_DIR) if f.lower().endswith(('.png', '.jpg', '.jpeg'))]
    output_files = os.listdir(OUTPUT_DIR)
    
    # Check that we have output files
    assert len(output_files) > 0, "The processing finished, but the output folder is empty."
    
    # Check that we have MORE output files than input files 
    # (Since you run 5 filters per image, you should have 5x the files)
    # Note: This assumes your filters save separate files (e.g. img_blur.jpg, img_canny.jpg)
    expected_min_files = len(input_files)
    assert len(output_files) >= expected_min_files, \
        f"Expected at least {expected_min_files} output files, but found {len(output_files)}."
        
    print(f"\nSuccess! Processed {len(input_files)} input images into {len(output_files)} output files.")