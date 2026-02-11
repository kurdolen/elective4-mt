import os
import pytest
from unittest.mock import patch, MagicMock
import process_image  # The module under test

# --- Fixtures ---
@pytest.fixture
def mock_directories(tmp_path):
    input_dir = tmp_path / "input"
    output_dir = tmp_path / "output"
    input_dir.mkdir()
    
    valid_image = input_dir / "test_image.jpg"
    valid_image.write_text("fake image content")
    
    text_file = input_dir / "readme.txt"
    text_file.write_text("this should be ignored")
    
    return str(input_dir), str(output_dir), str(valid_image)

# --- Test Cases ---

@patch('process_image.apply_four_filters') # New
@patch('process_image.apply_five_filters') # New
@patch('process_image.apply_bilateral_filter')
@patch('process_image.apply_emboss_filter')
@patch('process_image.apply_canny_edge')
@patch('process_image.apply_grayscale')
@patch('process_image.apply_median_blur')
def test_process_images_workflow(mock_blur, mock_gray, mock_edge, mock_emboss, mock_bilateral, mock_five, mock_four, mock_directories):
    input_dir, output_dir, img_path = mock_directories

    # Patch the directory constants in the process_image module
    with patch.object(process_image, 'INPUT_DIR', input_dir), \
         patch.object(process_image, 'OUTPUT_DIR', output_dir):
        
        # --- EXECUTE ---
        # Note: Updated function name from process_images() to process_image()
        process_image.process_image()

        # --- ASSERTIONS ---
        assert os.path.exists(output_dir)

        # Verify all 7 filters were called
        mock_blur.assert_called_once_with(img_path, output_folder=output_dir)
        mock_gray.assert_called_once_with(img_path, output_folder=output_dir)
        mock_edge.assert_called_once_with(img_path, output_folder=output_dir)
        mock_emboss.assert_called_once_with(img_path, output_folder=output_dir)
        mock_bilateral.assert_called_once_with(img_path, output_folder=output_dir)
        
        # Verify new combined filters
        mock_five.assert_called_once_with(img_path, output_dir)
        mock_four.assert_called_once_with(img_path, output_dir)

def test_process_images_no_files(tmp_path):
    input_dir = tmp_path / "input"
    output_dir = tmp_path / "output"
    input_dir.mkdir()

    with patch('process_image.apply_median_blur') as mock_blur, \
         patch.object(process_image, 'INPUT_DIR', str(input_dir)), \
         patch.object(process_image, 'OUTPUT_DIR', str(output_dir)):
        
        process_image.process_image()
        
        mock_blur.assert_not_called()