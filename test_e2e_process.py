import os
import cv2
import numpy as np
import pytest
from unittest.mock import patch
import process_image

@pytest.fixture
def real_image_env(tmp_path):
    input_dir = tmp_path / "input"
    output_dir = tmp_path / "output"
    input_dir.mkdir()
    
    # Generate dummy image
    img_array = np.random.randint(0, 255, (100, 100, 3), dtype=np.uint8)
    img_filename = "real_test_image.jpg"
    img_path = input_dir / img_filename
    cv2.imwrite(str(img_path), img_array)
    
    return input_dir, output_dir, img_path

def test_full_processing_pipeline(real_image_env):
    input_dir, output_dir, img_path = real_image_env

    with patch.object(process_image, 'INPUT_DIR', str(input_dir)), \
         patch.object(process_image, 'OUTPUT_DIR', str(output_dir)):
        
        # --- EXECUTE ---
        print(f"\nProcessing real image at: {img_path}")
        
        # Updated function name call
        process_image.process_image()
        
        # --- ASSERTIONS ---
        files_in_output = os.listdir(str(output_dir))
        assert len(files_in_output) > 0, "No output files created."
        
        print(f"Generated {len(files_in_output)} output files: {files_in_output}")

        for filename in files_in_output:
            file_path = os.path.join(str(output_dir), filename)
            processed_img = cv2.imread(file_path)
            
            assert processed_img is not None, f"Output file {filename} is corrupted."
            h, w, _ = processed_img.shape
            assert h == 100 and w == 100, f"Output image {filename} has wrong dimensions."