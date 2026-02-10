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
```bash
python -m pip install -r requirements.txt
```

## 📋 Requirements

- opencv-python
- numpy

## 📚 Project Structure

```
elective4-mt/
├── process_image.py          # Main runner that applies individual and chained filters
├── requirements.txt          # Python dependencies
├── README.md                 # Project documentation (this file)
├── test_real_data.py         # Simple test harness used during development
├── input/                    # Place input images here
├── output/                   # Processed images are written here
└── module/                   # Image processing modules and combiners
   ├── bilateral_filter.py
   ├── canny_edge.py
   ├── combine_filters.py    # Combined/sequential filter helpers
   ├── emboss_filter.py
   ├── grayscale.py
   └── median_blur.py
```

## 🚀 How to Run

1. **Prepare Input Images**
   - Place your image files in the `input/` directory
   - Supported formats: `.png`, `.jpg`, `.jpeg`, `.bmp`, `.tiff`

2. **Run the image pipeline**
```bash
python process_image.py
```

3. **Check Output**
   - Processed images will be saved in the `output/` directory
   - The runner creates individual outputs for each filter and also combined results
   - Typical filenames produced:
     - `<name>_median_blur<ext>`
     - `<name>_grayscale<ext>`
     - `<name>_canny<ext>` (module uses `_canny`)
     - `<name>_emboss<ext>`
     - `<name>_bilateral<ext>`
     - `<name>_combined<ext>` (final chained result created by `process_image.py`)
     - `<name>_00_FiveFilters<ext>` and `<name>_00_FourFilters<ext>` (helpers in `module/combine_filters.py`)

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
