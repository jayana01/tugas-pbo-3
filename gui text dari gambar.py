import tkinter as tk
from tkinter import ttk, filedialog
from PIL import Image, ImageTk
import pytesseract
from googletrans import Translator

class TextTranslationApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Text Translation App")
        self.root.geometry("600x500")

        self.translator = Translator()

        self.create_widgets()

    def create_widgets(self):
        # Label
        self.label = tk.Label(self.root, text="Text Translation App", font=("Helvetica", 16))
        self.label.pack(pady=10)

        # Tombol untuk memilih file gambar
        self.browse_button = ttk.Button(self.root, text="Pilih File Gambar", command=self.browse_image)
        self.browse_button.pack(pady=20)

        # Tampilan gambar yang dipilih
        self.image_label = tk.Label(self.root)
        self.image_label.pack()

        # Tombol untuk melakukan konversi teks dan terjemahan
        self.convert_button = ttk.Button(self.root, text="Konversi Teks dan Terjemahkan", command=self.convert_and_translate)
        self.convert_button.pack(pady=10)

        # Teks hasil konversi dan terjemahan
        self.result_text = tk.Text(self.root, height=10, width=50)
        self.result_text.pack(pady=10)

    def browse_image(self):
        # Membuka dialog untuk memilih file gambar
        file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg;*.gif")])

        # Menyimpan path file gambar yang dipilih
        self.image_path = file_path

        # Menampilkan gambar di label
        image = Image.open(file_path)
        image.thumbnail((300, 300))
        photo = ImageTk.PhotoImage(image)
        self.image_label.config(image=photo)
        self.image_label.image = photo

    def convert_and_translate(self):
        try:
            # Membaca teks dari gambar menggunakan pytesseract
            text = pytesseract.image_to_string(Image.open(self.image_path))
            
            # Menerjemahkan teks ke bahasa Inggris
            translated_text = self.translator.translate(text, dest='en').text
            
            # Menampilkan hasil konversi dan terjemahan di TextArea
            result = f"Teks dari Gambar:\n{text}\n\nTerjemahan:\n{translated_text}"
            self.result_text.delete(1.0, tk.END)
            self.result_text.insert(tk.END, result)

        except Exception as e:
            tk.messagebox.showinfo("Error", f"Terjadi kesalahan: {str(e)}")

if __name__ == "__main__":
    root = tk.Tk()
    text_translator = TextTranslationApp(root)
    root.mainloop()
