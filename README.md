# Elective 4 MidTerm (DevOps Application)

**DevOps** application for batch image processing with multiple filters and effects.

## Overview

This application processes images from an input directory, applies various image processing filters, and saves the results to an output directory. Features include median blur, grayscale conversion, Canny edge detection, emboss filter, and bilateral filtering.

## 🛠️ Setup & Installation

### Prerequisites

- **Python 3.10+** (Recommended)
- **pip** (Python package manager)

### Installation Steps

1. **Clone the Repository**
```bash
git clone <repository_url>
cd elective4-mt
```

2. **Install Dependencies (if not installed)** 
```bash
pip install -r requirements.txt
```
or
``bash
python -m pip install -r requirements.txt
``

## 📋 Requirements

- opencv-python
- numpy

## 📚 Project Structure

```
elective4-mt/
├── process_image.py          # Main script to run image processing
├── requirements.txt          # Python dependencies
├── README.md                 # Project documentation
├── input/                    # Directory for input images
├── output/                   # Directory for processed images
└── module/                   # Image processing modules
    ├── bilateral_filter.py
    ├── canny_edge.py
    ├── emboss_filter.py
    ├── grayscale.py
    └── median_blur.py
```

## 🚀 How to Run

1. **Prepare Input Images**
   - Place your image files in the `input/` directory
   - Supported formats: `.png`, `.jpg`, `.jpeg`, `.bmp`, `.tiff`

2. **Run the Image Processing Script**
```bash
python process_image.py
```

3. **Check Output**
   - Processed images will be saved in the `output/` directory
   - Each filter creates a separate processed image

## 📊 Filters Applied

The application applies the following image processing techniques:

- **Median Blur**: Reduces noise while preserving edges
- **Grayscale**: Converts color images to grayscale
- **Canny Edge Detection**: Detects edges in images
- **Emboss Filter**: Creates an embossing effect
- **Bilateral Filter**: Smooths images while keeping edges sharp

## 📝 Notes

- Ensure the `input/` and `output/` directories exist (they are created automatically if missing)
- Processing time depends on image size and quantity
- Check console output for processing status and any errors
