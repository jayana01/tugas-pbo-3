from PIL import Image
import pytesseract

# Tentukan path ke executable Tesseract OCR
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'  
# Sesuaikan dengan path instalasi Tesseract di komputer Anda

def extract_text_from_image(image_path):
    try:
        # Buka gambar menggunakan modul PIL
        image = Image.open(image_path)

        # Ekstrak teks menggunakan pytesseract
        text = pytesseract.image_to_string(image)

        return text
    except Exception as e:
        return f"Error: {e}"

if __name__ == "__main__":
    # lokasi file
    image_path = r'C:\Users\ruswa\OneDrive\Pictures\KENALAN.PNG'  
    extracted_text = extract_text_from_image(image_path)

    print("Extracted Text:")
    print(extracted_text)