import tkinter as tk
from tkinter import filedialog, messagebox
from pdf2md import pdf_to_md_images
from gui_helpers import browse_pdf, browse_output, start_conversion

app = tk.Tk()
app.title("PDF to Markdown Converter")

frame = tk.Frame(app, padx=20, pady=20)
frame.pack(padx=10, pady=10)

pdf_label = tk.Label(frame, text="Select PDF File:")
pdf_label.grid(row=0, column=0, sticky=tk.W)

pdf_entry = tk.Entry(frame, width=50)
pdf_entry.grid(row=0, column=1, padx=5, pady=5)

pdf_button = tk.Button(frame, text="Browse...", command=browse_pdf)
pdf_button.grid(row=0, column=2, padx=5, pady=5)

output_label = tk.Label(frame, text="Select Output Directory:")
output_label.grid(row=1, column=0, sticky=tk.W)

output_entry = tk.Entry(frame, width=50)
output_entry.grid(row=1, column=1, padx=5, pady=5)

output_button = tk.Button(frame, text="Browse...", command=browse_output)
output_button.grid(row=1, column=2, padx=5, pady=5)

convert_button = tk.Button(frame, text="Convert PDF", command=start_conversion, bg="blue", fg="white")
convert_button.grid(row=2, columnspan=3, pady=10)

app.mainloop()
