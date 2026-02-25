import os
import fitz  # PyMuPDF

DIR = "./test_files" # the directory

import os
import fitz  # PyMuPDF

def process_pdfs(directory):
    # Path for the output merged PDF
    output_path = os.path.join(directory, "new.pdf")
    output_pdf = fitz.open()

    # List all PDF files in the directory, excluding the output file itself
    pdf_files = [
        f for f in os.listdir(directory)
        if f.lower().endswith(".pdf") and f != "new.pdf"
    ]
    pdf_files.sort()

    # A4 portrait size in points (approx 595 x 842)
    A4_WIDTH, A4_HEIGHT = 595, 842

    for pdf_name in pdf_files:
        pdf_path = os.path.join(directory, pdf_name)
        src_pdf = fitz.open(pdf_path)
        
        # Skip empty PDFs
        if len(src_pdf) == 0:
            src_pdf.close()
            continue
        
        # Use the first page of each PDF (assumed A5 landscape)
        page = src_pdf[0]

        # Create a new A4 portrait page
        new_page = output_pdf.new_page(width=A4_WIDTH, height=A4_HEIGHT)

        # Top half of A4: A5 landscape area
        top_rect = fitz.Rect(
            0,
            0,
            A4_WIDTH,
            A4_HEIGHT / 2
        )

        # Bottom half of A4: A5 landscape area
        bottom_rect = fitz.Rect(
            0,
            A4_HEIGHT / 2,
            A4_WIDTH,
            A4_HEIGHT
        )

        # Draw the same A5 page twice (top and bottom)
        new_page.show_pdf_page(top_rect, src_pdf, 0)
        new_page.show_pdf_page(bottom_rect, src_pdf, 0)

        src_pdf.close()

    # Save the final merged PDF
    output_pdf.save(output_path)
    output_pdf.close()

    print(f"Done. Output saved as: {output_path}")


if __name__ == "__main__":
    # Read directory path from user input
    directory = DIR
    process_pdfs(directory)
