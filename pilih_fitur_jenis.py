from tkinter import *

class main_root():
    def __init__(self):
        self.root = Tk() # Membuat jendela utama

    def main_window(self):
        self.root.title("Taru Tama") # Judul jendela

        # Mengatur warna latar belakang jendela
        self.root.configure(bg="#436651")

        screen_width = self.root.winfo_screenwidth() # Lebar layar pengguna
        screen_height = self.root.winfo_screenheight() # Tinggi layar pengguna
        window_width = 400 # Lebar jendela
        window_height = 640 # Tinggi jendela

        # Menghitung posisi jendela agar berada di tengah layar
        root_width = (screen_width - window_width) // 2
        root_height = ((screen_height - window_height) // 2) - (round(screen_height*0.05))

        self.root.geometry(f"{window_width}x{window_height}+{root_width}+{root_height}") # Lebar x Tinggi + Posisi X + Posisi Y

        self.root.resizable(False, False)  # Mencegah jendela diubah ukurannya tetapi tetap dapat dipindahkan selapangnya layar

    def button_features(self):

        # Label untuk kalkulator karbon
        self.label = Label(
            self.root, 
            text="KALKULATOR\nKARBON",
            fg="#000000",
            bg="#436651",
            font=("Arial", 18, "bold"),
            justify="right",
            anchor="e")
        self.label.place(
            relx=0.5,
            rely=0.1)

        # Tombol untuk kembali ke halaman pilih_fitur
        self.button_kembali_pilih_fitur = Button(
            self.root, text="<<<<",
            width=5, height=2, bg="#DEE693",
            fg="#000000",
            font=("Arial", 12),
            anchor="center")
        self.button_kembali_pilih_fitur.place(
            relx=0.1,
            rely=0.1,)

        # Tombol untuk fitur kalkulator
        self.button_kendaraan = Button(
            self.root, text="Kendaraan",
            width=20, height=2, bg="#DEE693",
            fg="#000000",
            font=("Arial", 12))
        self.button_kendaraan.place(
            relx=0.5,
            rely=0.45,
            anchor="center")

        # Tombol untuk fitur donasi
        self.button_elektronika = Button(
            self.root,
            text="Elektronika",
            width=20,
            height=2,
            bg="#DEE693",
            fg="#000000",
            font=("Arial", 12))
        self.button_elektronika.place(
            relx=0.5,
            rely=0.6,
            anchor="center")

    def run_window(self):
        self.root.mainloop() #menjalankan program

class run_program():
    def __init__(self):
        call_main_root = main_root() # Memanggil class main_root
        call_main_root.main_window() # Memanggil fungsi main_window
        call_main_root.button_features() # Memanggil fungsi button_features
        call_main_root.run_window() # Menjalankan program

run_program = run_program() # Membuat instance class run_program
run_program # Memanggil class run_program