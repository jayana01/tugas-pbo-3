import pygame

def main():
    # lokasi file musik 
    file_path = r'C:\Users\ruswa\Downloads\suara_burung.mp3' 

    try:
        # Inisialisasi Pygame
        pygame.init()  
        
        # Setel lokasi file musik
        pygame.mixer.music.load(file_path) 
        
        # Putar musik
        pygame.mixer.music.play()

        # Tunggu hingga musik selesai diputar
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)

    except Exception as e:
        print(f"Gagal memainkan file musik: {e}")

    finally:
        #Matikan pygame
        pygame.quit() 

if __name__ == "__main__":
    main()
        