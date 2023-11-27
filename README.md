# PDF Table Extractor and Image Converter with OCR

This Python script is a versatile tool that allows users to extract text and tables from PDFs and images, using Optical Character Recognition (OCR) technology. It supports both PDFs and various image formats and is based on the GPT-3.5 version and organic intelligence.

I thought it was a good idea to have an offline tool to convert .pdf or images that we anybody wants to upload to a server. So here is a simple solution.

## Features

- Extract text from PDF files and images.
- Extract tables from PDFs using Camelot.
- Save extracted text to a CSV file.
- Save extracted tables to an Excel file.

## Prerequisites

- Python 3.x installed
- Tesseract-OCR installed
- Necessary Python packages installed (`pytesseract`, `Pillow`, `PyPDF2`, `camelot`, `pandas`)

## Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/your_username/pdf-image-converter.git
    ```

2. **Install required Python packages:**

    ```bash
    pip install pytesseract Pillow PyPDF2 camelot-py[cv] pandas
    ```

3. **Install Tesseract-OCR:**

    Download and install Tesseract-OCR from the [official repository](https://github.com/tesseract-ocr/tesseract).

4. **Set Tesseract-OCR path (Update in the code):**

    ```python
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
    ```

## Usage

1. Run the `main.py` file.
2. Click on the "Select File and Convert" button.
3. Choose the file you want to convert.
4. Choose the destination folder to save the converted files.

## Acknowledgements

This program was developed with the help of GPT-3.5 and organic intelligence.



