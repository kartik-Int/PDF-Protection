import sys
from PyPDF2 import PdfReader,PdfWriter  # type: ignore

# Create a Python script that accepts command-line inputs.
def cretae_password_protected_pdf(input_pdf, output_pdf, password):
    try:
        # Open and read the input PDF file.
        with open(input_pdf, "rb") as f:
            pdf_reader = PdfReader(f)
            page_count = len(pdf_reader.pages)
            # print(f"{input_pdf} has {page_count} pages")


            # Copy the content of the original PDF to a new PdfWriter object.
            pdf_writer = PdfWriter()
            for page_num in range(page_count):
                pdf_writer.add_page(pdf_reader.pages[page_num])


            # Apply encryption using the encrypt() method.
            pdf_writer.encrypt(password)


            # Save the encrypted file and provide user feedback.
            with open(output_pdf, "wb") as out_f:
                pdf_writer.write(out_f)
            print(f"Encrypted Successfully and saved as {output_pdf}")


    # Implement error handling to manage missing or corrupt PDF files.
    except FileNotFoundError:
        print(f"{input_pdf} not found")
    except Exception as e:
        print(f"Unexpected error: {e}")


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python script.py <input_pdf> <output_pdf> <password>")
        sys.exit(1)
    cretae_password_protected_pdf(input_pdf=sys.argv[1],output_pdf=sys.argv[2],password=sys.argv[3])
