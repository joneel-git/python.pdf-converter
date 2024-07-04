import tkinter as tk
from tkinter import filedialog, messagebox
import os

def browse_pdf(pdf_entry):
    pdf_path = filedialog.askopenfilename(filetypes=[("PDF Files", "*.pdf")])
    pdf_entry.delete(0, tk.END)
    pdf_entry.insert(0, pdf_path)

def browse_output(output_entry):
    output_path = filedialog.askdirectory()
    output_entry.delete(0, tk.END)
    output_entry.insert(0, output_path)

def start_conversion(pdf_entry, output_entry, pdf_to_md_images):
    pdf_path = pdf_entry.get()
    output_dir = output_entry.get()
    if not pdf_path or not output_dir:
        messagebox.showwarning("Input Error", "Please provide both PDF and output paths.")
        return

    md_output = os.path.join(output_dir, "output.md")
    media_folder = os.path.join(output_dir, "images")

    try:
        pdf_to_md_images(pdf_path, md_output, media_folder)
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")
