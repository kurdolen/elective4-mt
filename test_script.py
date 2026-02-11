import os
import pytest
import cv2
import numpy as np
import process_image

@pytest.fixture
def setup_input_folder():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    input_dir = os.path.join(base_dir, "input")
    
    if not os.path.exists(input_dir):
        os.makedirs(input_dir)

    files = [f for f in os.listdir(input_dir) if f.endswith(('.jpg', '.png', '.jpeg'))]
    
    if not files:
        print("\n[Setup] No images found. Creating a dummy test image...")
        dummy_img = np.zeros((100, 100, 3), dtype=np.uint8)
        dummy_img[:] = (0, 0, 255)
        cv2.imwrite(os.path.join(input_dir, "test_dummy.jpg"), dummy_img)
    
    return input_dir

def test_full_automation_pipeline(setup_input_folder):
    input_dir = setup_input_folder
    
    print("\n[Action] Running the image processing script...")
    
    process_image.process_image()
    
    output_dir = os.path.join(os.path.dirname(input_dir), "output")
    assert os.path.exists(output_dir), "Test Failed: Output folder was not created!"
    
    input_count = len([f for f in os.listdir(input_dir) if f.endswith(('.jpg', '.png', '.jpeg'))])
    output_files = os.listdir(output_dir)
    output_count = len(output_files)
    
    expected_min = input_count * 7
    
    assert output_count >= expected_min, \
        f"Test Failed: Expected at least {expected_min} output files, but found {output_count}."
        
    print(f"\n[Success] Pipeline works! Processed {input_count} images into {output_count} output files.")