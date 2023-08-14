#!/usr/bin/env python
import os
from pypdf import PdfReader
from typing import List


def convert_pdf_to_txt(file_path: str) -> None:
    base_name, _ = os.path.splitext(file_path)

    # Check if directory for the PDF exists and if not, create one
    output_dir = base_name
    os.makedirs(output_dir, exist_ok=True)

    reader = PdfReader(file_path)
    if all(os.path.exists(os.path.join(output_dir, f"{os.path.basename(base_name)}_page_{index + 1}.txt"))
           for index in range(len(reader.pages))):
        print(f"Skipped (already converted): {file_path}")
        return

    try:
        print(f"Converting: {file_path}")

        for index, page in enumerate(reader.pages):
            txt_file_path = os.path.join(output_dir, f"{os.path.basename(base_name)}_page_{index + 1}.txt")

            # Skip if the txt file for this page already exists
            if os.path.exists(txt_file_path):
                print(f"Skipped (page already converted): {txt_file_path}")
                continue

            txt_content = page.extract_text()
            if txt_content:
                with open(txt_file_path, "w", encoding="utf-8") as text_file:
                    text_file.write(txt_content)
                print(f"Saved: {txt_file_path}")
            else:
                print(f"No text content in page {index + 1} of {file_path}")

    except Exception as e:
        print(f"Error converting {file_path}. Reason: {e}")


def botrun_pdf_to_text_single_file(file_path: str) -> None:
    if file_path.endswith(".pdf"):
        convert_pdf_to_txt(file_path)
    else:
        print(f"Not a PDF file: {file_path}")


def botrun_pdf_to_text_files(file_list: List[str]) -> None:
    for file_path in file_list:
        botrun_pdf_to_text_single_file(file_path)


def botrun_pdf_to_text_folder(folder_path: str) -> None:
    for root, _, files in os.walk(folder_path):
        for file in files:
            if file.endswith(".pdf"):
                botrun_pdf_to_text_single_file(os.path.join(root, file))


if __name__ == "__main__":
    botrun_pdf_to_text_folder("./users/cbh_cameo_tw/data/upload_files")
    botrun_pdf_to_text_files(["./users/cbh_cameo_tw/data/upload_files/222715345.pdf"])
    botrun_pdf_to_text_single_file("./users/cbh_cameo_tw/data/upload_files/222715345.pdf")
