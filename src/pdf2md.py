import os
import pdfplumber
import fitz
from tkinter import messagebox

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
        image_list = page.getImageList()

        for image_index, img in enumerate(image_list, start=1):
            xref = img[0]
            base_image = pdf_doc.extract_image(xref)
            image_bytes = base_image["image"]
            image_ext = base_image["ext"]
            image_filename = f"image_page_{page_num}_img_{image_index}.{image_ext}"
            image_path = os.path.join(media, image_filename)

            with open(image_path, "wb") as image_file:
                image_file.write(image_bytes)

    pdf_doc.close()
    messagebox.showinfo("Success", "PDF conversion completed successfully!")
