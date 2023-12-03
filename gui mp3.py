import os
import tkinter as tk
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QFileDialog
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from tkinter import filedialog
from pygame import mixer


class MusicPlayer:
    def __init__(self, root):
        self.root = root
        self.root.title("MP3 Player")
        self.root.geometry("400x150")

        mixer.init()  # Inisialisasi modul pygame.mixer

        self.create_widgets()

    def create_widgets(self):
        # Label
        self.label = tk.Label(self.root, text="MP3 Player", font=("Helvetica", 16))
        self.label.pack(pady=10)

        # Tombol untuk memilih file MP3
        self.browse_button = tk.Button(self.root, text="Pilih File MP3", command=self.browse_file)
        self.browse_button.pack(pady=20)

        # Tombol untuk memutar file MP3
        self.play_button = tk.Button(self.root, text="Putar", command=self.play_music)
        self.play_button.pack(pady=10)

    def browse_file(self):
        # Membuka dialog untuk memilih file MP3
        file_path = filedialog.askopenfilename(filetypes=[("MP3 Files", "*.mp3")])

        # Menyimpan path file MP3 yang dipilih
        self.file_path = file_path

        # Menampilkan nama file di label
        self.label["text"] = os.path.basename(file_path)

    def play_music(self):
        try:
            mixer.music.load(self.file_path)
            mixer.music.play()
        except AttributeError:
            tk.messagebox.showinfo("Info", "Pilih file MP3 terlebih dahulu.")

if __name__ == "__main__":
    root = tk.Tk()
    music_player = MusicPlayer(root)
    root.mainloop()
