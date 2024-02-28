from PyPDF2 import PdfReader as pr 
from PyPDF2 import PdfWriter as pw
from PyPDF2 import PdfMerger as pm
import os

def info_pdf(pdf_path):
    with open(pdf_path, "rb") as file:
        pdf = pr(file)
        info = pdf.metadata
    return info

def extract_text_from_pdf(pdf_path):
    with open(pdf_path, "rb") as file:
        pdf = pr(file)
        results = []
        for page in pdf.pages:
            text = page.extract_text()
            results.append(text)
        return " ".join(results)
    
def split_pdf_pages(pdf_path):
    i = 1
    with open(pdf_path, "rb") as file:
        pdf = pr(file)
        # get all pages
        for page in pdf.pages:
            # writer to write
            writer = pw()
            writer.add_page(page)
            filename = os.path.splitext(pdf_path)[0]
            output_filename = f"form_{filename}_page_{i}.pdf"
            # save and compile to pdf
            with open(output_filename, "wb") as out:
                writer.write(out)
            print(f"created a pdf:{output_filename}")
            i = i + 1
    
def pdf_pages_upto(pdf_path, start_page: int=0, end_page: int=0):
    with open(pdf_path, "rb") as file:
        pdf = pr(file)
        writer = pw()
        for page_num in range(start_page, end_page):
            current_page = pdf.pages[page_num]
            writer.add_page(current_page)
        filename = os.path.splitext(pdf_path)[0]
        output_filename = f"{filename}_from_{start_page}_to_{end_page -1}.pdf"
        with open(output_filename, "wb") as out:
            writer.write(out)

def split_pdf_last_page(pdf_path):
    with open(pdf_path, "rb") as file:
        pdf = pr(file)
        writer = pw()
        current_page = pdf.pages[len(pdf.pages)-1]
        writer.add_page(current_page)
    filename = os.path.splitext(pdf_path)[0]
    output_filename = f"{filename}_last_page.pdf"
    with open(output_filename, "wb") as out:
        writer.write(out)
    print("Splited the last page of pdf")
        
def fetch_pdfs_form_dir(parant_folder_path):
    pdfs = []
    for path, subdirs, files in os.walk(parant_folder_path):
        for name in files:
            if name.endswith(".pdf"):
                pdfs.append(os.path.join(path, name))
    return pdfs

def merge_pdfs(list_of_pdfs, output_filename = "final_merged_pdf.pdf"):
    merger = pm()
    with open(output_filename, "wb") as file:
        for pdf in list_of_pdfs:
            merger.append(pdf)
        merger.write(file)
    print("Merged all pdfs")

def rotate_pdf_page(pdf_path, page_num, rotation: int = 90):
    with open(pdf_path, "rb") as file:
        pdf = pr(file)
        writer = pw()
        writer.add_page(pdf.pages[page_num])
        # rotate the page
        writer.pages[page_num].rotate(rotation)
        filename = os.path.splitext(pdf_path)[0]
        output_filename = f"{filename}_page_{page_num}_rotated_{rotation}'.pdf"
        with open(output_filename, "wb") as out:
            writer.write(out)
        print("pdf page rotated")


