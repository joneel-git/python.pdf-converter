import os
import pdfplumber
import fitz
import tkinter as tk
from tkinter import filedialog, messagebox

# Function to remove unnecessary whitespace and replace with backslash
def remove_whitespace(text):
    return "\\".join(text.split())

# PDF to Markdown conversion with images
def pdf_to_md_images(pdf_path, md_output, media):
    os.makedirs(media, exist_ok=True)

    markdown_text = ""

    with pdfplumber.open(pdf_path) as pdf:
        for i, page in enumerate(pdf.pages):
            page_text = page.extract_text()
            markdown_text += f"## Page {i+1}\n\n"
            if page_text:
                markdown_text += page_text + "\n\n"

    with open(md_output, "w", encoding="utf-8") as file:
        file.write(markdown_text)

    pdf_doc = fitz.open(pdf_path)

    for page_num in range(len(pdf_doc)):
        page = pdf_doc.load_page(page_num)
        image_list = page.get_images(full=True)

        for image_index, img_info in enumerate(image_list, start=1):
            xref = img_info[0]
            base_image = pdf_doc.extract_image(xref)
            image_bytes = base_image["image"]
            image_ext = base_image["ext"]
            image_filename = f"image_page_{page_num}_img_{image_index}.{image_ext}"
            image_path = os.path.join(media, image_filename)

            with open(image_path, "wb") as image_file:
                image_file.write(image_bytes)

    pdf_doc.close()
    messagebox.showinfo("Success", "PDF conversion completed successfully!")

# Browse PDF file
def browse_pdf():
    pdf_path = filedialog.askopenfilename(filetypes=[("PDF Files", "*.pdf")])
    pdf_entry.delete(0, tk.END)
    pdf_entry.insert(0, pdf_path)

# Browse output directory
def browse_output():
    output_path = filedialog.askdirectory()
    output_entry.delete(0, tk.END)
    output_entry.insert(0, output_path)

# Start PDF to Markdown conversion
def start_conversion():
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

# GUI setup
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
