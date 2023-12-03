import cv2
import tkinter as tk
from tkinter import ttk, filedialog

class VideoPlayer:
    def __init__(self, root):
        self.root = root
        self.root.title("MP4 Player")
        self.root.geometry("600x400")

        self.create_widgets()

    def create_widgets(self):
        # Label
        self.label = tk.Label(self.root, text="MP4 Player", font=("Helvetica", 16))
        self.label.pack(pady=10)

        # Tombol untuk memilih file MP4
        self.browse_button = ttk.Button(self.root, text="Pilih File MP4", command=self.browse_file)
        self.browse_button.pack(pady=20)

        # Tombol untuk memutar video
        self.play_button = ttk.Button(self.root, text="Putar Video", command=self.play_video)
        self.play_button.pack(pady=10)

    def browse_file(self):
        # Membuka dialog untuk memilih file MP4
        file_path = filedialog.askopenfilename(filetypes=[("MP4 Files", "*.mp4")])

        # Menyimpan path file MP4 yang dipilih
        self.file_path = file_path

        # Menampilkan nama file di label
        self.label["text"] = file_path

    def play_video(self):
        try:
            # Membuka file video
            cap = cv2.VideoCapture(self.file_path)

            # Membaca frame pertama
            ret, frame = cap.read()

            # Menampilkan video dalam jendela GUI
            while ret:
                cv2.imshow("Video Player", frame)
                ret, frame = cap.read()
                if cv2.waitKey(28) & 0xFF == ord("q"):
                    break

            # Menghentikan pemutaran video dan menutup jendela ketika selesai
            cap.release()
            cv2.destroyAllWindows()

        except cv2.error:
            tk.messagebox.showinfo("Info", "Pilih file MP4 terlebih dahulu.")

if __name__ == "__main__":
    root = tk.Tk()
    video_player = VideoPlayer(root)
    root.mainloop()
