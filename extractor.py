import pdfplumber


class Extractor:

    # extract text from the PDF
    def text_from_pdf(self, pdf_file):
        text = None

        # handling exceptions
        try:
            # extract text from pdf
            with pdfplumber.open(pdf_file) as pdf:
                for page in pdf.pages:
                    text += page.extract_text()


        except Exception as e:
            print(f"Error reading PDF: {e}")

        return text
