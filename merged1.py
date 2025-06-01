import tkinter as tk
from tkinter import messagebox
import math
import os
import json
from PIL import ImageTk, Image

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Ksatria Taru")
        
        # Set window size and position it in center
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        window_width = 400
        window_height = 640
        x = (screen_width // 2) - (window_width // 2)
        y = (screen_height // 2) - (window_height // 2) - 30  # Slightly higher than center

        self.root.geometry(f"{window_width}x{window_height}+{x}+{y}")
        self.root.resizable(False, False)

        self.container = tk.Frame(self.root)
        self.container.place(relx=0, rely=0, relwidth=1, relheight=1)
        
        self.pages = {}
        self.current_page = None
        self.create_pages()
        self.show_page("start")

    def create_pages(self):
        self.pages["start"] = InChoice(self.container, self.show_page)
        self.pages["login"] = LoginPage(self.container, self.show_page)
        self.pages["signup"] = SignupPage(self.container, self.show_page)
        self.pages["main_menu"] = MainMenu(self.container, self.show_page)
        self.pages["kalkulator"] = KalkulatorKarbon(self.container, self.show_page)
        self.pages["transportasi"] = KarbonTransportasi(self.container, self.show_page)
        self.pages["elektronik"] = KarbonElektronika(self.container, self.show_page)
        self.pages["donasi"] = Donasi(self.container, self.show_page)
        self.pages["hasil_emisi"] = HasilEmisi(self.container, self.show_page)
        self.pages["qris"] = QrisPage(self.container, self.show_page)

    def show_page(self, page_name, data=None):
        if page_name == "hasil_emisi":
            self.pages["hasil_emisi"] = HasilEmisi(self.container, self.show_page, data)
        
        if self.current_page:
            self.current_page.frame.lower()
        
        self.current_page = self.pages[page_name]
        self.current_page.frame.tkraise()

class InChoice:
    def __init__(self, container, show_page):
        self.container = container
        self.show_page = show_page
        self.create_widgets()

    def create_widgets(self):
        self.frame = tk.Frame(self.container, bg="#DEE693")
        self.frame.place(relx=0, rely=0, relwidth=1, relheight=1)

        tk.Label(self.frame, text="Selamat\nDatang,\nKsatria Taru!", bg="#DEE693", font=("Inter", 17), justify="center").place(relx=0.5, y=80, anchor="center")

        tk.Canvas(self.frame, width=50, height=80, bg="#436651", highlightthickness=0).place(relx=0.5, y=200, anchor="center")

        tk.Button(self.frame, text="Login", bg="white", command=self.show_login, relief="flat", font=("Inter", 10, "bold")).place(relx=0.5, rely=0.6, anchor="center", width=150, height=35)

        tk.Button(self.frame, text="Sign Up", bg="white", command=self.show_signup, relief="flat", font=("Inter", 10, "bold")).place(relx=0.5, rely=0.67, anchor="center", width=150, height=35)

    def show_login(self):
        self.show_page("login")

    def show_signup(self):
        self.show_page("signup")

class LoginPage:
    def __init__(self, container, show_page):
        self.container = container
        self.show_page = show_page
        self.create_widgets()

    def create_widgets(self):
        self.frame = tk.Frame(self.container, bg="#CADFC4")
        self.frame.place(x=0, y=0, width=412, height=717)

        header = tk.Frame(self.frame, bg="#2f4f3c", height=100)
        header.pack(fill="x")

        tk.Button(header, text="<", command=lambda: self.show_page("start"), bg="#2f4f3c", fg="white", relief="flat").place(x=5, y=5)

        form = tk.Frame(self.frame, bg="#8ba98f")
        form.pack(fill="both", expand=True)

        tk.Label(form, text="Login", bg="#8ba98f", font=("Inter", 12, "bold")).pack(pady=20)

        tk.Label(form, text="Alamat Email:", bg="#8ba98f").pack(anchor="w", padx=20)
        self.login_email = tk.Entry(form)
        self.login_email.pack(padx=20, fill="x")

        tk.Label(form, text="Password:", bg="#8ba98f").pack(anchor="w", padx=20, pady=(10, 0))
        self.login_password = tk.Entry(form, show="*")
        self.login_password.pack(padx=20, fill="x")

        tk.Button(form, text="Login", bg="white", font=("Inter", 10, "bold"), command=self.login).pack(pady=10, ipadx=10, ipady=2)

        tk.Label(form, text="Belum punya akun?", bg="#8ba98f").pack(side="left", padx=(30, 2), pady=10)
        tk.Button(form, text="Sign Up", bg="#8ba98f", fg="blue", font=("Inter", 9, "bold"), relief="flat", command=lambda: self.show_page("signup")).pack(side="left")

    def login(self):
        email = self.login_email.get()
        password = self.login_password.get()

        filename = os.path.join("data_akun", f"{email.replace('@','_at_')}.json")
        if os.path.exists(filename):
            with open(filename, "r") as f:
                data = json.load(f)
                if data["password"] == password:
                    self.login_email.delete(0, tk.END)
                    self.login_password.delete(0, tk.END)
                    self.show_page("main_menu")
                else:
                    messagebox.showerror("Error", "Password salah!")
        else:
            messagebox.showerror("Error", "Email tidak ditemukan!")

class SignupPage:
    def __init__(self, container, show_page):
        self.container = container
        self.show_page = show_page
        self.create_widgets()

    def create_widgets(self):
        self.frame = tk.Frame(self.container, bg="#436651")
        self.frame.place(x=0, y=0, width=412, height=717)

        header = tk.Frame(self.frame, bg="#8ba98f", height=100)
        header.pack(fill="x")

        tk.Button(header, text="<", command=lambda: self.show_page("start"), bg="#8ba98f", fg="black", relief="flat").place(x=5, y=5)

        form = tk.Frame(self.frame, bg="#2f4f3c")
        form.pack(fill="both", expand=True)

        tk.Label(form, text="Sign Up", bg="#2f4f3c", fg="white", font=("Inter", 12, "bold")).pack(pady=20)

        tk.Label(form, text="Nama:", bg="#2f4f3c", fg="white").pack(anchor="w", padx=20)
        self.entry_nama = tk.Entry(form)
        self.entry_nama.pack(padx=20, fill="x")

        tk.Label(form, text="Alamat Email:", bg="#2f4f3c", fg="white").pack(anchor="w", padx=20, pady=(10, 0))
        self.entry_email = tk.Entry(form)
        self.entry_email.pack(padx=20, fill="x")

        tk.Label(form, text="Password:", bg="#2f4f3c", fg="white").pack(anchor="w", padx=20, pady=(10, 0))
        self.entry_password = tk.Entry(form, show="*")
        self.entry_password.pack(padx=20, fill="x")

        tk.Button(form, text="Sign Up", bg="white", font=("Inter", 10, "bold"), command=self.sign_up).pack(pady=10, ipadx=10, ipady=2)

        tk.Label(form, text="Sudah punya akun?", bg="#2f4f3c", fg="white").pack(side="left", padx=(30, 2), pady=10)
        tk.Button(form, text="Login", bg="#2f4f3c", fg="lightblue", font=("Inter", 9, "bold"), relief="flat", command=lambda: self.show_page("login")).pack(side="left")

    def sign_up(self):
        nama = self.entry_nama.get()
        email = self.entry_email.get()
        password = self.entry_password.get()

        if not nama or not email or not password:
            messagebox.showerror("Error", "Semua field harus diisi!")
            return

        data = {
            "nama": nama,
            "email": email,
            "password": password
        }

        if not os.path.exists("data_akun"):
            os.makedirs("data_akun")

        filename = os.path.join("data_akun", f"{email.replace('@','_at_')}.json")
        with open(filename, "w") as f:
            json.dump(data, f, indent=4)

        messagebox.showinfo("Success", f"Akun untuk {email} telah dibuat.")
        self.entry_nama.delete(0, tk.END)
        self.entry_email.delete(0, tk.END)
        self.entry_password.delete(0, tk.END)

        self.show_page("start")

class MainMenu:
    def __init__(self, container, show_page):
        self.container = container
        self.show_page = show_page
        self.create_widgets()

    def create_widgets(self):
        self.frame = tk.Frame(self.container, bg="#DEE693")
        self.frame.place(relx=0, rely=0, relwidth=1, relheight=1)

        kembali_btn = tk.Button(self.frame, text="<<<<", command=lambda: self.show_page("start"), width=5, height=2, bg="#8FC07C", fg="#0A2736", font=("Inter", 12), anchor="center")
        kembali_btn.place(relx=0.05, rely=0.035)

        kalkulator_btn = tk.Button(self.frame, text="KALKULATOR KARBON", command=lambda: self.show_page("kalkulator"), width=20, height=2, bg="#8FC07C", fg="#0A2736", font=("Inter", 12))
        kalkulator_btn.place(relx=0.3, rely=0.45, anchor="center")

        donasi_btn = tk.Button(self.frame, text="DONASI", command=lambda: self.show_page("donasi"), width=20, height=2, bg="#8FC07C", fg="#0A2736", font=("Inter", 12))
        donasi_btn.place(relx=0.7, rely=0.6, anchor="center")

        keluar_btn = tk.Button(self.frame, text="KELUAR", command=self.keluar, width=20, height=2, bg="#8FC07C", fg="#0A2736", font=("Inter", 12))
        keluar_btn.place(relx=0.3, rely=0.75, anchor="center")

    def keluar(self):
        self.show_page("start")

class KalkulatorKarbon:
    def __init__(self, container, show_page):
        self.container = container
        self.show_page = show_page
        self.create_widgets()

    def create_widgets(self):
        self.frame = tk.Frame(self.container, bg="#436651")
        self.frame.place(relx=0, rely=0, relwidth=1, relheight=1)

        label = tk.Label(self.frame, text="KALKULATOR\nKARBON", fg="#DEE693", bg="#436651", font=("Inter", 18, "bold"), justify="right", anchor="e")
        label.place(relx=0.5, rely=0.1)

        kembali_btn = tk.Button(self.frame, text="<<<<", command=lambda: self.show_page("main_menu"), width=5, height=2, bg="#DEE693", fg="#0A2736", font=("Inter", 12), anchor="center")
        kembali_btn.place(relx=0.05, rely=0.035)

        tombol_kendaraan = tk.Button(self.frame, text="Kendaraan", width=20, height=2, bg="#DEE693", fg="#0A2736", font=("Inter", 12), command=lambda: self.show_page("transportasi"))
        tombol_kendaraan.place(relx=0.3, rely=0.45, anchor="center")

        tombol_elektronik = tk.Button(self.frame, text="Elektronik", command=lambda: self.show_page("elektronik"), width=20, height=2, bg="#DEE693", fg="#0A2736", font=("Inter", 12))
        tombol_elektronik.place(relx=0.7, rely=0.6, anchor="center")

class KarbonTransportasi: # demo (percobaan)
    def __init__(self, container, show_page):
        self.container = container
        self.show_page = show_page
        self.create_widgets()

    def create_widgets(self):
        self.frame = tk.Frame(self.container)
        self.frame.place(relx=0, rely=0, relwidth=1, relheight=1)

        label = tk.Label(self.frame, text="TRANSPORTASI", fg="#0A2736", 
                       font=("Inter", 18, "bold"), anchor="center")
        label.place(relx=0.5, rely=0.135, anchor="center")

        fields = [
            ("Jenis Kendaraan", "jenis", 0.250, 0.325),
            ("Jarak Tempuh (km)", "jarak", 0.350, 0.425),
            ("Frekuensi (kali/minggu)", "frekuensi", 0.450, 0.525)
        ]

        self.entries = {}
        for text, name, rely_label, rely_entry in fields:
            label = tk.Label(self.frame, text=text, fg="#0A2736", font=("Inter", 12, "bold"), justify="left", anchor="w")
            label.place(relx=0.25, rely=rely_label)

            entry = tk.Entry(self.frame, bg="#D9D9D9", fg="#0A2736", font=("Inter", 12))
            entry.place(relx=0.5, rely=rely_entry, anchor="center", width=200, height=30)
            self.entries[name] = entry

        hitung_btn = tk.Button(self.frame, text="Hitung", command=self.hitung_emisi, width=20, height=2, bg="#D9D9D9", fg="#0A2736", font=("Inter", 12))
        hitung_btn.place(relx=0.5, rely=0.725, anchor="center")

        kembali_btn = tk.Button(self.frame, text="KEMBALI", command=lambda: self.show_page("kalkulator"), width=20, height=2, bg="#D9D9D9", fg="#0A2736", font=("Inter", 12))
        kembali_btn.place(relx=0.5, rely=0.825, anchor="center")

    def hitung_emisi(self):
        try:
            jenis = self.entries["jenis"].get()
            jarak = float(self.entries["jarak"].get())
            frekuensi = int(self.entries["frekuensi"].get())

            factors = {
                "Mobil": 0.2,
                "Motor": 0.1,
                "Bus": 0.05
            }
            
            factor = factors.get(jenis, 0.15)
            total_emisi = jarak * frekuensi * 4 * factor
            pohon = math.ceil(total_emisi / 25)
            
            self.show_page("hasil_emisi", {"emisi": total_emisi, "pohon": pohon})
            
        except ValueError:
            messagebox.showerror("Error", "Input tidak valid")

class KarbonElektronika:
    def __init__(self, container, show_page):
        self.container = container
        self.show_page = show_page
        self.create_widgets()

    def create_widgets(self):
        self.frame = tk.Frame(self.container)
        self.frame.place(x=0, y=0, width=412, height=717)

        label = tk.Label(self.frame, text="ELEKTRONIK", fg="#0A2736", font=("Inter", 18, "bold"), anchor="center")
        label.place(relx=0.5, rely=0.135, anchor="center")

        fields = [
            ("Daya Perangkat (watt)", "daya", 0.250, 0.325),
            ("Jumlah Perangkat", "jumlah", 0.350, 0.425),
            ("Durasi (jam)", "durasi", 0.450, 0.525),
            ("Frekuensi (Hari)", "frekuensi", 0.550, 0.625)
        ]

        self.entries = {}
        for text, name, rely_label, rely_entry in fields:
            label = tk.Label(self.frame, text=text, fg="#0A2736", font=("Inter", 12, "bold"), justify="left", anchor="w")
            label.place(relx=0.25, rely=rely_label)
            
            entry = tk.Entry(self.frame, bg="#D9D9D9", fg="#0A2736", font=("Inter", 12))
            entry.place(relx=0.5, rely=rely_entry, anchor="center", width=200, height=30)
            self.entries[name] = entry

        hitung_btn = tk.Button(self.frame, text="Hitung", command=self.hitung_emisi, width=20, height=2, bg="#D9D9D9", fg="#0A2736", font=("Inter", 12))
        hitung_btn.place(relx=0.5, rely=0.725, anchor="center")

        kembali_btn = tk.Button(self.frame, text="KEMBALI", command=lambda: self.show_page("kalkulator"), width=20, height=2, bg="#D9D9D9", fg="#0A2736", font=("Inter", 12))
        kembali_btn.place(relx=0.5, rely=0.825, anchor="center")

    def hitung_emisi(self):
        try:
            daya = float(self.entries["daya"].get())
            jumlah = int(self.entries["jumlah"].get())
            durasi = float(self.entries["durasi"].get())
            frekuensi = int(self.entries["frekuensi"].get())

            total_emisi = (daya * jumlah * durasi * frekuensi) / 1000
            pohon = math.ceil(total_emisi / 25)
            
            self.show_page("hasil_emisi", {"emisi": total_emisi, "pohon": pohon})
            
        except ValueError:
            messagebox.showerror("Error", "Input tidak valid")

class Donasi:
    def __init__(self, container, show_page):
        self.container = container
        self.show_page = show_page
        self.entry_var = tk.IntVar()
        self.label_var = tk.IntVar()
        self.create_widgets()

    def create_widgets(self):
        self.frame = tk.Frame(self.container, bg="#436651")
        self.frame.place(x=0, y=0, width=412, height=717)

        label_judul = tk.Label(self.frame, text="DONASI", fg="#DEE693", bg="#436651", font=("Inter", 18, "bold"))
        label_judul.place(relx=0.5, rely=0.135, anchor="center")

        label_harga = tk.Label(self.frame, text="1 Pohon = Rp. 20.000", fg="#0A2736", 
                             bg="#DEE693", font=("Inter", 12, "bold"), justify="left")
        label_harga.place(relx=0.5, rely=0.25, width=250, height=50, anchor="center")

        label_pohon = tk.Label(self.frame, text="Pohon", fg="#0A2736", bg="#DEE693", font=("Inter", 12, "bold"))
        label_pohon.place(relx=0.523, rely=0.35, width=115, height=50, anchor="w")

        self.entry_var.trace_add("write", self.hitung_donasi)
        
        entry_pohon = tk.Entry(self.frame, justify="center", textvariable=self.entry_var, bg="#DEE693", fg="#0A2736", font=("Inter", 12, "bold"))
        entry_pohon.place(relx=0.187, rely=0.35, relwidth=0.1, anchor="w", width=80, height=50)

        label_rupiah = tk.Label(self.frame, text="Rp.", fg="#0A2736", bg="#DEE693", font=("Inter", 12, "bold"), anchor="center")
        label_rupiah.place(relx=0.187, rely=0.45, relwidth=0.1, anchor="w", width=80, height=50)

        label_jumlah = tk.Label(self.frame, textvariable=self.label_var, fg="#0A2736", bg="#DEE693", font=("Inter", 12, "bold"), anchor="center")
        label_jumlah.place(relx=0.523, rely=0.45, width=115, height=50, anchor="w")

        tombol_donasi = tk.Button(self.frame, text="BAYAR", command=lambda: self.show_page("qris"), width=20, height=2, bg="#D9D9D9", fg="#0A2736", font=("Inter", 12))
        tombol_donasi.place(relx=0.5, rely=0.725, anchor="center")

        kembali_btn = tk.Button(self.frame, text="KEMBALI", command=lambda: self.show_page("main_menu"), width=20, height=2, bg="#D9D9D9", fg="#0A2736", font=("Inter", 12))
        kembali_btn.place(relx=0.5, rely=0.825, anchor="center")

    def hitung_donasi(self, *args):
        try:
            input_pengguna = self.entry_var.get()
            if input_pengguna == 0:
                self.label_var.set(0)
            else:
                total_donasi = input_pengguna * 20000
                self.label_var.set(total_donasi)
        except ValueError:
            self.label_var.set(0)

class HasilEmisi:
    def __init__(self, container, show_page, data=None):
        self.container = container
        self.show_page = show_page
        self.data = data or {"emisi": 0, "pohon": 0}
        self.create_widgets()

    def create_widgets(self):
        self.frame = tk.Frame(self.container, bg="#18656A")
        self.frame.place(x=0, y=0, width=412, height=717)

        label_narasi_emisi = tk.Label(self.frame, text="EMISI\nKarbon Anda:", bg="#18656A", fg="#DEE693", font=("Inter", 18, "bold"), justify="left")
        label_narasi_emisi.place(relx=0.5, rely=0.175, anchor="e")

        label_emisi = tk.Label(self.frame, text=f"{self.data['emisi']:.2f}", bg="#DEE693", fg="#0A2736", font=("Inter", 18, "bold"), justify="left", padx=5, pady=5)
        label_emisi.place(relx=0.1, rely=0.26, width=220, height=45, anchor="w")

        label_satuan_emisi = tk.Label(self.frame, text="KG", bg="#DEE693", fg="#0A2736", font=("Inter", 18, "bold"), justify="right")
        label_satuan_emisi.place(relx=0.9, rely=0.26, width=85, height=45, anchor="e")

        label_narasi_pohon = tk.Label(self.frame, text="Membutuhkan:", bg="#18656A", fg="#DEE693", font=("Inter", 18, "bold"), justify="left")
        label_narasi_pohon.place(relx=0.535, rely=0.435, anchor="e")

        label_pohon = tk.Label(self.frame, text=f"{self.data['pohon']}", bg="#DEE693", fg="#0A2736", font=("Inter", 18, "bold"), justify="left", padx=5, pady=5)
        label_pohon.place(relx=0.1, rely=0.5, width=220, height=45, anchor="w")

        label_satuan_pohon = tk.Label(self.frame, text="Pohon", bg="#DEE693", fg="#0A2736", font=("Inter", 18, "bold"), justify="right")
        label_satuan_pohon.place(relx=0.9, rely=0.5, width=85, height=45, anchor="e")

        donasi_btn = tk.Button(self.frame, text="DONASI", command=lambda: self.show_page("donasi"), width=20, height=2, bg="#D9D9D9", fg="#0A2736", font=("Inter", 12))
        donasi_btn.place(relx=0.5, rely=0.725, anchor="center")

        kembali_btn = tk.Button(self.frame, text="KEMBALI", command=lambda: self.show_page("main_menu"), width=20, height=2, bg="#D9D9D9", fg="#0A2736", font=("Inter", 12))
        kembali_btn.place(relx=0.5, rely=0.825, anchor="center")

class QrisPage:
    def __init__(self, container, show_page):
        self.container = container
        self.show_page = show_page
        self.create_widgets()

    def create_widgets(self):
        self.frame = tk.Frame(self.container, bg="#18656A")
        self.frame.place(x=0, y=0, width=412, height=717)

        label_judul = tk.Label(self.frame, text="BAYAR", fg="#DEE693", bg="#18656A", font=("Inter", 18, "bold"))
        label_judul.place(relx=0.5, rely=0.135, anchor="center")
        
        label_subjudul = tk.Label(self.frame, text="Scan Barcode di bawah ini", fg="#DEE693", bg="#18656A", font=("Inter", 12, "bold"))
        label_subjudul.place(relx=0.5, rely=0.185, anchor="center")

        try:
            img = Image.open("qris_barcode.png")
            img = img.resize((280, 280))
            img = ImageTk.PhotoImage(img)
            label = tk.Label(self.frame, image=img, bg="#18656A", bd=1.5, relief="solid")
            label.image = img
            label.place(relx=0.5, rely=0.43, anchor="center")
        except FileNotFoundError:
            label = tk.Label(self.frame, text="Gambar QRIS tidak ditemukan\nPastikan gambar file berada di repositori yang sama", fg="#DEE693", bg="#18656A", font=("Arial", 12))
            label.place(relx=0.5, rely=0.5, anchor="center")

        cek_status_btn = tk.Button(self.frame, text="Cek Status Pembayaran", command=self.cek_status, width=20, height=2, bg="#D9D9D9", fg="#0A2736", font=("Inter", 12))
        cek_status_btn.place(relx=0.5, rely=0.725, anchor="center")

        kembali_btn = tk.Button(self.frame, text="KEMBALI", command=lambda: self.show_page("main_menu"), width=20, height=2, bg="#D9D9D9", fg="#0A2736", font=("Inter", 12))
        kembali_btn.place(relx=0.5, rely=0.825, anchor="center")

    def cek_status(self):
        messagebox.showinfo("Status Pembayaran", "Donasi Berhasil Terkirim🎉🎉🎉")

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
