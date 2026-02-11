# 📷 Automated Image Processing Pipeline

![Python](https://img.shields.io/badge/Python-3.x-blue?style=flat-square&logo=python)
![OpenCV](https://img.shields.io/badge/OpenCV-Computer%20Vision-green?style=flat-square&logo=opencv)
![Pytest](https://img.shields.io/badge/Testing-Pytest-yellow?style=flat-square&logo=pytest)

## 📌 Project Overview
This project is a Python-based image processing automation tool designed to streamline the application of various computer vision techniques. The system monitors an `input/` directory, detects valid image files, and processes them through a pipeline of five distinct filters before saving the results to an `output/` directory.

This application was developed as a school assignment to demonstrate modular Python programming, file system manipulation, and image processing using OpenCV.

## 🚀 Key Features
The application automatically applies the following techniques to every image found in the input directory:

1.  **Median Blur:** Reduces noise while effectively preserving edges.
2.  **Grayscale Conversion:** Converts color images to black and white for structural analysis.
3.  **Canny Edge Detection:** Identifies strong structural edges within the image.
4.  **Emboss Filter:** Creates a 3D shadow effect, highlighting high-frequency details.
5.  **Bilateral Filter:** Smoothes images while keeping edges sharp (advanced noise reduction).

## 📂 Project Structure
```text
Project/
├── .github/workflows       # chore: setup github actions pipeline
├── input/                  # Place raw images here (.jpg, .png, etc.)
├── output/                 # Processed images will appear here
├── module/                 # Image processing modules
│   ├── median_blur.py
│   ├── grayscale.py
│   ├── canny_edge.py
│   ├── emboss_filter.py
│   ├── bilateral_filter.py
│   └── combine_filters.py
├── process_image.py        # Main execution script
├── test_process_image.py   # Unit/Integration tests (Mocked)
├── test_e2e_process.py     # End-to-End system tests (Generated data)
├── test_real_data.py       # Real data smoke tests (Actual input files)
├── requirements.txt        # Project dependencies
└── README.md               # Project documentation
```

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
## 💻 Usage

1. Add Images: Place your raw images (.jpg, .png, .jpeg, .bmp, or .tiff) into the input/ folder.
2. Run the Script: Execute the main processing script:
   python process_image.py
3. View Results: Check the output/ folder. You will see processed versions of your images (e.g., image_canny.jpg, image_blur.jpg).

## 🧪 Testing Documentation
This project includes a robust testing suite using Pytest, covering logic, system behavior, and real-world data.

1. Integration Tests (Mocked)
   File: test_process_image.py
   Purpose: Verifies the logic (e.g., "Does it detect files?", "Does it call the filter functions?").
   Method: Uses Mocking to skip heavy image processing.
   Run Command:
   python -m pytest test_process_image.py -v

2. End-to-End System Tests
   File: test_end2end_process.py

3. Real Data Smoke Tests
   File: test_real_data.py
   Purpose: Verifies the deployment (e.g., "Does it work on MY specific images?").
   Method: Processes actual files from your input/ folder.
   Run Command:
   python -m pytest test_real_data.py -s -v

## ⚡ Run All Tests
To execute the entire test suite at once:
python -m pytest -v


## ⚠️ Academic Integrity
This project was developed as a school assignment.
For Students: Please use this code for reference and learning purposes only. Do not copy the code directly to submit as your own work.

## 📝 Authors
### Asuncion, Andrei T. - Developer
### De Leon, John Eron R. - DevOps
### Apolonio, Lanz Matthew B. - Automated QA Tester
### Ponelas, Joshua Efraim O. - Presenter