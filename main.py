import pytesseract
from PIL import Image
import os
import io
import PyPDF2
import csv
import camelot
import pandas as pd
import tkinter as tk
from tkinter import filedialog


# Path to the Tesseract-OCR executable (change this according to your system)
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def extract_text_from_image(image_path):
    # Open the image using PIL (Python Imaging Library)
    image = Image.open(image_path)
    
    # Use pytesseract to do OCR on the image
    text = pytesseract.image_to_string(image)
    
    return text

def extract_text_from_pdf(pdf_path):
    # Open the PDF file in read-binary mode
    with open(pdf_path, 'rb') as file:
        pdf_reader = PyPDF2.PdfReader(file)
        
        # Initialize an empty list to store extracted lines
        lines = []
        
        # Loop through each page and extract text
        for page_num in range(len(pdf_reader.pages)):
            page = pdf_reader.pages[page_num]
            
            # Extract text from the page and split it into lines
            page_text = page.extract_text()
            page_lines = page_text.split('\n')
            
            # Append each line to the list
            lines.extend(page_lines)
        
        return lines

# Modify the extract_text function to use extract_text_from_pdf in case of a PDF file
def extract_text(file_path):
    if file_path.endswith('.pdf'):
        lines = extract_text_from_pdf(file_path)
        return lines
    else:
        return extract_text_from_image(file_path)


def extract_tables_from_pdf(pdf_path):
    # Extract tables from the PDF using Camelot
    tables = camelot.read_pdf(pdf_path, flavor='stream', pages='all')
    
    return tables

def save_tables_to_excel(tables, excel_path):
    # Create an Excel file and save the tables as separate sheets
    with pd.ExcelWriter(excel_path) as writer:
        for i, table in enumerate(tables):
            table.df.to_excel(writer, sheet_name=f'Table_{i+1}', index=False)

def convert_and_save():
    file2Convert = filedialog.askopenfilename(title="Select file to convert")
    if not file2Convert:
        return  # Exit function if no file selected
    
    file_lines = extract_text(file2Convert)
    file_name, _ = os.path.splitext(os.path.basename(file2Convert))
    extracted_tables = extract_tables_from_pdf(file2Convert)
    
    # Choose the destination folder to save the files
    destination_folder = filedialog.askdirectory(title="Select destination folder")
    if not destination_folder:
        destination_folder = os.path.dirname(file2Convert)  # Use the original folder if no destination selected
    
    # Define the output file paths
    excel_file_path = os.path.join(destination_folder, f'{file_name}.xlsx')
    csv_file = os.path.join(destination_folder, f'{file_name}.csv')
    
    # Save tables to Excel and text lines to CSV
    save_tables_to_excel(extracted_tables, excel_file_path)
    with open(csv_file, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Extracted Line'])
        for line in file_lines:
            writer.writerow([line])

    print(f'Tables have been extracted and saved to {excel_file_path}')
    print(f'Text lines have been saved to {csv_file}')

# Create a simple GUI using tkinter
root = tk.Tk()
root.title("File Converter")

# Create a button to start the conversion
convert_button = tk.Button(root, text="Select File and Convert", command=convert_and_save)
convert_button.pack()

root.mainloop()
