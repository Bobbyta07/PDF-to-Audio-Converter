from converter import Converter
from extractor import Extractor

convert = Converter()
extract = Extractor()

if __name__ == "__main__":
    # Specify PDF file path here
    pdf_file = ''

    # Extract text from the PDF
    text = extract.text_from_pdf(pdf_file)

    if text:
        # Convert extracted text to speech and save it as an MP3
        output_file = 'output_audio.mp3'
        convert.text_to_speech(text, output_file)
    else:
        print("No text extracted from PDF.")
