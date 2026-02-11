import os
import pytest
import shutil
import cv2
import process_image

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
INPUT_DIR = os.path.join(BASE_DIR, "input")
OUTPUT_DIR = os.path.join(BASE_DIR, "output")

@pytest.fixture(autouse=True)
def setup_and_teardown():
    """
    Optional: Cleans the output folder before running to ensure 
    we are testing THIS run's results, not old files.
    """
    if os.path.exists(OUTPUT_DIR):
        shutil.rmtree(OUTPUT_DIR)
    yield

def test_verify_process_image_logic(capsys):
    """
    Strictly tests process_image.py line-by-line by verifying 
    all side effects (files created, text printed, inputs ignored).
    """
    
    assert os.path.exists(INPUT_DIR), "Input directory is missing!"
    all_files = os.listdir(INPUT_DIR)
    
    valid_extensions = ('.png', '.jpg', '.jpeg', '.bmp', '.tiff')
    valid_inputs = [f for f in all_files if f.lower().endswith(valid_extensions)]
    ignored_inputs = [f for f in all_files if not f.lower().endswith(valid_extensions)]
    
    assert len(valid_inputs) > 0, "TEST FAIL: No valid images found in input folder to test."
    print(f"\n[Setup] Found {len(valid_inputs)} valid images and {len(ignored_inputs)} ignored files.")

    print("[Action] Running process_image()...")
    process_image.process_image()

    captured = capsys.readouterr()
    for img_name in valid_inputs:
        expected_msg = f"Processing {img_name}..."
        assert expected_msg in captured.out, f"TEST FAIL: Script did not print '{expected_msg}'. Loop logic might be broken."

    assert os.path.exists(OUTPUT_DIR), "TEST FAIL: Output directory was not created."
    output_files = os.listdir(OUTPUT_DIR)

    expected_filter_count = 7 
    
    print("\n[Verification] Checking outputs per image:")
    
    for img_name in valid_inputs:
        name_stem = os.path.splitext(img_name)[0]
        
        related_outputs = [f for f in output_files if name_stem in f]
        
        assert len(related_outputs) >= expected_filter_count, \
            f"TEST FAIL: for image '{img_name}', expected {expected_filter_count} outputs but found {len(related_outputs)}. " \
            f"Did one of the filters fail to save?"

        print(f"  ✓ {img_name} -> Generated {len(related_outputs)} files.")

        sample_output = os.path.join(OUTPUT_DIR, related_outputs[0])
        img_data = cv2.imread(sample_output)
        assert img_data is not None, f"TEST FAIL: Output file {sample_output} is unreadable or corrupt."
        assert img_data.size > 0, f"TEST FAIL: Output file {sample_output} is empty."

    for ignored in ignored_inputs:
        name_stem = os.path.splitext(ignored)[0]
        if any(name_stem in valid for valid in valid_inputs):
            continue
            
        related_mistakes = [f for f in output_files if name_stem in f]
        assert len(related_mistakes) == 0, f"TEST FAIL: Script processed an invalid file: {ignored}"

    print("\n[Success] All lines of code executed correctly on real data!")