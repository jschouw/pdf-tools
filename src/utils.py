#!/usr/bin/env python3

"""
    Functionality and logic of the program, including both GUI creation and PDF manipulation.
"""


# [brainstorming:]
# functionality to-do: splice, split, metadata operations, extract text, extract images,
# encrypt/password, reduce file size
# Edit text and images, reorder, and delete pages in a PDF
# Convert PDFs and export to Microsoft Word, Excel, and PowerPoint
# Redact to permanently remove sensitive visible information
# Compare two versions of a PDF to review all differences

# ****************************************************************************

import os
from datetime import datetime
from pypdf import PdfReader
from pypdf import PdfWriter
from tkinter import messagebox
from tkinter import filedialog


def splice_pdfs():
    return print("splice_pdfs function called")


def extract_text():
    return print("extract_text function called")


def extract_images():
    return print("extract_images function called")


def merge_pdfs():
    """Allows the user to select multiple files to merge, as well as what order to merge them in."""

    valid = False
    while not valid:  # 'not' checks for false boolean value
        file = filedialog.askopenfilenames( # Open file choosing dialog window
            filetypes=[("PDF files", "*.pdf")],
            title="Please select files to merge:",
            initialdir=os.getcwd())

        if not file:  # If file returns false the cancel button was pressed, so nothing and return to main menu
            return 1

        if len(file) <= 1:  # More than 1 file must be chosen to merge
            messagebox.showerror(title="Error: Not enough files chosen",
                                 message="Error: You must choose more than 1 file to merge.")
        else:
            pdf_writer = PdfWriter()

            for filename in file:
                pdf_reader = PdfReader(filename)  # Read the PDF
                pdf_writer.append(fileobj=pdf_reader)  # Write the PDF to the Writer object by appending to end of file

            current_time = str(datetime.now().strftime("%Y-%m-%d-%H-%M-%S"))  # Get current time for unique filename
            output = open(current_time + "-merged_output.pdf", "wb")  # Open the file to write to
            pdf_writer.write(output)  # Write the PdfWriter object to the open file
            pdf_writer.close()
            return messagebox.showinfo(title="Merge successful",
                                       message="Files merged successfully.")
