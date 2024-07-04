import fitz
import os
from PIL import Image

def pdf_to_images(pdf_path, output_folder):
    pdf_document = fitz.open(pdf_path)

    for page_num in range(len(pdf_document)):
        page = pdf_document.load_page(page_num)

        pix = page.get_pixmap()
        img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)

        pdf_name = os.path.splitext(os.path.basename(pdf_path))[0]
        output_path = os.path.join(output_folder, f"{pdf_name}_page_{page_num + 1}.png")

        img.save(output_path)

        print(f"Saved{output_path}")

    pdf_document.close()

def process_pdf_directory(input_folder, output_folder):

    os.makedirs(output_folder, exist_ok=True)
    

    for file_name in os.listdir(input_folder):
        if file_name.endswith('.pdf'):
            pdf_path = os.path.join(input_folder, file_name)
            print(f"Processing {pdf_path}")
            pdf_to_images(pdf_path, output_folder)


input_folder = "<INPUT FOLDER PATH>"
output_folder = "<OUTPUT FOLDER PATH>" 

process_pdf_directory(input_folder, output_folder)
