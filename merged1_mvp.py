import tkinter as tk
from tkinter import messagebox
import math
import os
import json
import requests
from io import BytesIO
from PIL import ImageTk, Image

# Model
class Model:
    def __init__(self):
        self.user_data = None
        self.carbon_data = None
        self.donation_data = None

    def login_user(self, email, password):
        filename = os.path.join("data_akun", f"{email.replace('@','_at_')}.json")
        if os.path.exists(filename):
            with open(filename, "r") as f:
                data = json.load(f)
                if data["password"] == password:
                    self.user_data = data
                    return True, "Login berhasil!"
                else:
                    return False, "Password salah!"
        else:
            return False, "Email tidak ditemukan!"

    def register_user(self, nama, email, password):
        if not nama or not email or not password:
            return False, "Semua field harus diisi!"

        data = {
            "nama": nama,
            "email": email,
            "password": password
        }

        if not os.path.exists("data_akun"):
            os.makedirs("data_akun")

        filename = os.path.join("data_akun", f"{email.replace('@','_at_')}.json")
        if os.path.exists(filename):
            return False, "Email sudah terdaftar!"

        with open(filename, "w") as f:
            json.dump(data, f, indent=4)

        self.user_data = data
        return True, f"Akun untuk {email} telah dibuat."

    def calculate_transport_emission(self, jenis, jarak, frekuensi):
        factors = {
            "Mobil": 0.2,
            "Motor": 0.1,
            "Bus": 0.05
        }

        factor = factors.get(jenis, 0.15)
        total_emisi = jarak * frekuensi * 4 * factor
        pohon = math.ceil(total_emisi / 25)

        self.carbon_data = {"emisi": total_emisi, "pohon": pohon}
        return self.carbon_data

    def calculate_electronic_emission(self, daya, jumlah, durasi, frekuensi):
        total_emisi = (daya * jumlah * durasi * frekuensi) / 1000
        pohon = math.ceil(total_emisi / 25)

        self.carbon_data = {"emisi": total_emisi, "pohon": pohon}
        return self.carbon_data

    # Method Donasi
    def calculate_donation(self, jumlah_pohon):
        return jumlah_pohon * 20000

# View
class View:
    def __init__(self, root, controller):
        self.root = root
        self.controller = controller
        self.setup_window()
        self.create_pages()
        self.show_page("start")

    def setup_window(self):
        self.root.title("Ksatria Taru")

        # Set window size and position
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        window_width = 400
        window_height = 640
        x = (screen_width // 2) - (window_width // 2)
        y = (screen_height // 2) - (window_height // 2) - 30

        self.root.geometry(f"{window_width}x{window_height}+{x}+{y}")
        self.root.resizable(False, False)

        self.container = tk.Frame(self.root)
        self.container.place(relx=0, rely=0, relwidth=1, relheight=1)

        self.current_page = None
        self.pages = {}

    def create_pages(self):
        self.pages["start"] = StartPage(self.container, self.controller)
        self.pages["login"] = LoginPage(self.container, self.controller)
        self.pages["signup"] = SignupPage(self.container, self.controller)
        self.pages["main_menu"] = MainMenuPage(self.container, self.controller)
        self.pages["kalkulator"] = KalkulatorPage(self.container, self.controller)
        self.pages["transportasi"] = TransportasiPage(self.container, self.controller)
        self.pages["elektronik"] = ElektronikPage(self.container, self.controller)
        self.pages["donasi"] = DonasiPage(self.container, self.controller)
        self.pages["hasil_emisi"] = HasilEmisiPage(self.container, self.controller)
        self.pages["qris"] = QrisPage(self.container, self.controller)

    def show_page(self, page_name, data=None):
        if page_name == "hasil_emisi":
            self.pages["hasil_emisi"] = HasilEmisiPage(self.container, self.controller, data)

        if self.current_page:
            self.current_page.frame.lower()

        self.current_page = self.pages[page_name]
        self.current_page.frame.tkraise()

class StartPage:
    def __init__(self, container, controller):
        self.controller = controller
        self.frame = tk.Frame(container, bg="#DEE693")
        self.frame.place(relx=0, rely=0, relwidth=1, relheight=1)

        tk.Label(self.frame, text="Selamat\nDatang,\nKsatria Taru!", bg="#DEE693", font=("Inter", 17), justify="center").place(relx=0.5, y=80, anchor="center")

        tk.Canvas(self.frame, width=50, height=80, bg="#436651", highlightthickness=0).place(relx=0.5, y=200, anchor="center")

        tk.Button(self.frame, text="Login", bg="white", command=self.controller.show_login_page, relief="flat", font=("Inter", 10, "bold")).place(relx=0.5, rely=0.6, anchor="center", width=150, height=35)

        tk.Button(self.frame, text="Sign Up", bg="white", command=self.controller.show_signup_page, relief="flat", font=("Inter", 10, "bold")).place(relx=0.5, rely=0.67, anchor="center", width=150, height=35)

class LoginPage:
    def __init__(self, container, controller):
        self.controller = controller
        self.frame = tk.Frame(container, bg="#CADFC4")
        self.frame.place(x=0, y=0, width=412, height=717)

        header = tk.Frame(self.frame, bg="#2f4f3c", height=100)
        header.pack(fill="x")

        kembali_btn = tk.Button(self.frame, text="<<<<", command=self.controller.show_start_page, width=5, height=2, bg="#8ba98f", fg="#2f4f3c", font=("Inter", 12), anchor="center")
        kembali_btn.place(relx=0.05, rely=0.035)

        form = tk.Frame(self.frame, bg="#8ba98f")
        form.pack(fill="both", expand=True)

        tk.Label(form, text="Login", bg="#8ba98f", font=("Inter", 12, "bold")).pack(pady=20)

        tk.Label(form, text="Alamat Email:", bg="#8ba98f").pack(anchor="w", padx=20)
        self.login_email = tk.Entry(form)
        self.login_email.pack(padx=20, fill="x")

        tk.Label(form, text="Password:", bg="#8ba98f").pack(anchor="w", padx=20, pady=(10, 0))
        self.login_password = tk.Entry(form, show="*")
        self.login_password.pack(padx=20, fill="x")

        tk.Button(form, text="Login", bg="white", font=("Inter", 10, "bold"), command=self.handle_login).pack(pady=10, ipadx=10, ipady=2)

        tk.Label(form, text="Belum punya akun?", bg="#8ba98f").pack(side="left", padx=(30, 2), pady=10)
        tk.Button(form, text="Sign Up", bg="#8ba98f", fg="blue", font=("Inter", 9, "bold"), relief="flat", command=self.controller.show_signup_page).pack(side="left")

    def handle_login(self):
        email = self.login_email.get()
        password = self.login_password.get()
        self.controller.handle_login(email, password)

class SignupPage:
    def __init__(self, container, controller):
        self.controller = controller
        self.frame = tk.Frame(container, bg="#436651")
        self.frame.place(x=0, y=0, width=412, height=717)

        header = tk.Frame(self.frame, bg="#8ba98f", height=100)
        header.pack(fill="x")

        kembali_btn = tk.Button(self.frame, text="<<<<", command=self.controller.show_start_page, width=5, height=2, bg="#2f4f3c", fg="#8ba98f", font=("Inter", 12), anchor="center")
        kembali_btn.place(relx=0.05, rely=0.035)

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

        tk.Button(form, text="Sign Up", bg="white", font=("Inter", 10, "bold"), command=self.handle_signup).pack(pady=10, ipadx=10, ipady=2)

        tk.Label(form, text="Sudah punya akun?", bg="#2f4f3c", fg="white").pack(side="left", padx=(30, 2), pady=10)
        tk.Button(form, text="Login", bg="#2f4f3c", fg="lightblue", font=("Inter", 9, "bold"), relief="flat", command=self.controller.show_login_page).pack(side="left")

    def handle_signup(self):
        nama = self.entry_nama.get()
        email = self.entry_email.get()
        password = self.entry_password.get()
        self.controller.handle_signup(nama, email, password)

class MainMenuPage:
    def __init__(self, container, controller):
        self.controller = controller
        self.frame = tk.Frame(container, bg="#DEE693")
        self.frame.place(relx=0, rely=0, relwidth=1, relheight=1)

        kembali_btn = tk.Button(self.frame, text="<<<<", command=self.controller.logout, width=5, height=2, bg="#8FC07C", fg="#0A2736", font=("Inter", 12), anchor="center")
        kembali_btn.place(relx=0.05, rely=0.035)

        kalkulator_btn = tk.Button(self.frame, text="KALKULATOR KARBON", command=self.controller.show_kalkulator_page, width=20, height=2, bg="#8FC07C", fg="#0A2736", font=("Inter", 12))
        kalkulator_btn.place(relx=0.3, rely=0.45, anchor="center")

        donasi_btn = tk.Button(self.frame, text="DONASI", command=self.controller.show_donasi_page, width=20, height=2, bg="#8FC07C", fg="#0A2736", font=("Inter", 12))
        donasi_btn.place(relx=0.7, rely=0.6, anchor="center")

        keluar_btn = tk.Button(self.frame, text="KELUAR", command=self.controller.logout, width=20, height=2, bg="#8FC07C", fg="#0A2736", font=("Inter", 12))
        keluar_btn.place(relx=0.3, rely=0.75, anchor="center")

class KalkulatorPage:
    def __init__(self, container, controller):
        self.controller = controller
        self.frame = tk.Frame(container, bg="#436651")
        self.frame.place(relx=0, rely=0, relwidth=1, relheight=1)

        label = tk.Label(self.frame, text="KALKULATOR\nKARBON", fg="#DEE693", bg="#436651", font=("Inter", 18, "bold"), justify="right", anchor="e")
        label.place(relx=0.5, rely=0.1)

        kembali_btn = tk.Button(self.frame, text="<<<<", command=self.controller.show_main_menu_page, width=5, height=2, bg="#DEE693", fg="#0A2736", font=("Inter", 12), anchor="center")
        kembali_btn.place(relx=0.05, rely=0.035)

        tombol_kendaraan = tk.Button(self.frame, text="Kendaraan", width=20, height=2, bg="#DEE693", fg="#0A2736", font=("Inter", 12), command=self.controller.show_transportasi_page)
        tombol_kendaraan.place(relx=0.3, rely=0.45, anchor="center")

        tombol_elektronik = tk.Button(self.frame, text="Elektronik", command=self.controller.show_elektronik_page, width=20, height=2, bg="#DEE693", fg="#0A2736", font=("Inter", 12))
        tombol_elektronik.place(relx=0.7, rely=0.6, anchor="center")

class TransportasiPage:
    def __init__(self, container, controller):
        self.controller = controller
        self.frame = tk.Frame(container)
        self.frame.place(relx=0, rely=0, relwidth=1, relheight=1)

        label = tk.Label(self.frame, text="TRANSPORTASI", fg="#0A2736", font=("Inter", 18, "bold"), anchor="center")
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

        hitung_btn = tk.Button(self.frame, text="Hitung", command=self.handle_calculation, width=20, height=2, bg="#D9D9D9", fg="#0A2736", font=("Inter", 12))
        hitung_btn.place(relx=0.5, rely=0.725, anchor="center")

        kembali_btn = tk.Button(self.frame, text="KEMBALI", command=self.controller.show_kalkulator_page, width=20, height=2, bg="#D9D9D9", fg="#0A2736", font=("Inter", 12))
        kembali_btn.place(relx=0.5, rely=0.825, anchor="center")
    
    def handle_calculation(self):
        jenis = self.entries["jenis"].get()
        jarak = self.entries["jarak"].get()
        frekuensi = self.entries["frekuensi"].get()

        if not jenis or not jarak or not frekuensi:
            messagebox.showerror("Error", "Semua field harus diisi!")
            return

        try:
            jarak = float(jarak)
            frekuensi = int(frekuensi)
            self.controller.calculate_transport_emission(jenis, jarak, frekuensi)
        except ValueError:
            messagebox.showerror("Error", "Input tidak valid")

class ElektronikPage:
    def __init__(self, container, controller):
        self.controller = controller
        self.frame = tk.Frame(container)
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

        hitung_btn = tk.Button(self.frame, text="Hitung", command=self.handle_calculation, width=20, height=2, bg="#D9D9D9", fg="#0A2736", font=("Inter", 12))
        hitung_btn.place(relx=0.5, rely=0.725, anchor="center")

        kembali_btn = tk.Button(self.frame, text="KEMBALI", command=self.controller.show_kalkulator_page, width=20, height=2, bg="#D9D9D9", fg="#0A2736", font=("Inter", 12))
        kembali_btn.place(relx=0.5, rely=0.825, anchor="center")

    def handle_calculation(self):
        daya = self.entries["daya"].get()
        jumlah = self.entries["jumlah"].get()
        durasi = self.entries["durasi"].get()
        frekuensi = self.entries["frekuensi"].get()

        if not daya or not jumlah or not durasi or not frekuensi:
            messagebox.showerror("Error", "Semua field harus diisi!")
            return

        try:
            daya = float(daya)
            jumlah = int(jumlah)
            durasi = float(durasi)
            frekuensi = int(frekuensi)
            self.controller.calculate_electronic_emission(daya, jumlah, durasi, frekuensi)
        except ValueError:
            messagebox.showerror("Error", "Input tidak valid")

class DonasiPage:
    def __init__(self, container, controller):
        self.controller = controller
        self.entry_var = tk.StringVar()
        self.label_var = tk.IntVar()

        self.frame = tk.Frame(container, bg="#436651")
        self.frame.place(x=0, y=0, width=412, height=717)

        label_judul = tk.Label(self.frame, text="DONASI", fg="#DEE693", bg="#436651", font=("Inter", 18, "bold"))
        label_judul.place(relx=0.5, rely=0.135, anchor="center")

        label_harga = tk.Label(self.frame, text="1 Pohon = Rp. 20.000", fg="#0A2736", bg="#DEE693", font=("Inter", 12, "bold"), justify="left")
        label_harga.place(relx=0.5, rely=0.25, width=250, height=50, anchor="center")

        label_pohon = tk.Label(self.frame, text="Pohon", fg="#0A2736", bg="#DEE693", font=("Inter", 12, "bold"))
        label_pohon.place(relx=0.523, rely=0.35, width=115, height=50, anchor="w")

        self.entry_var.trace_add("write", self.handle_donation_calculation)

        vcmd = (self.frame.register(self.only_int), "%P")
        self.entry_pohon = tk.Entry(self.frame, justify="center", textvariable=self.entry_var, validate="key", validatecommand=vcmd, bg="#DEE693", fg="#0A2736", font=("Inter", 12, "bold"))
        self.entry_pohon.place(relx=0.187, rely=0.35, relwidth=0.1, anchor="w", width=80, height=50)

        self.entry_pohon.insert(0, "0")  # Placeholder
        self.entry_pohon.config(fg="#888888")

        self.entry_pohon.bind("<FocusIn>", lambda e: self.clear_placeholder())
        self.entry_pohon.bind("<FocusOut>", lambda e: self.restore_placeholder())

        label_rupiah = tk.Label(self.frame, text="Rp.", fg="#0A2736", bg="#DEE693", font=("Inter", 12, "bold"), anchor="center")
        label_rupiah.place(relx=0.187, rely=0.45, relwidth=0.1, anchor="w", width=80, height=50)

        label_jumlah = tk.Label(self.frame, textvariable=self.label_var, fg="#0A2736", bg="#DEE693", font=("Inter", 12, "bold"), anchor="center")
        label_jumlah.place(relx=0.523, rely=0.45, width=115, height=50, anchor="w")

        tombol_donasi = tk.Button(self.frame, text="BAYAR", command=self.handle_payment, width=20, height=2, bg="#D9D9D9", fg="#0A2736", font=("Inter", 12))
        tombol_donasi.place(relx=0.5, rely=0.725, anchor="center")

        kembali_btn = tk.Button(self.frame, text="KEMBALI", command=self.controller.show_main_menu_page, width=20, height=2, bg="#D9D9D9", fg="#0A2736", font=("Inter", 12))
        kembali_btn.place(relx=0.5, rely=0.825, anchor="center")

    def clear_placeholder(self):
        if self.entry_var.get() == "0":
            self.entry_pohon.delete(0, tk.END)
            self.entry_pohon.config(fg="#0A2736")

    def restore_placeholder(self):
        if not self.entry_var.get().strip():
            self.entry_var.set("0")
            self.entry_pohon.config(fg="#888888")

    def only_int(self, new_text):
        return new_text.isdigit() or new_text == ""

    def handle_donation_calculation(self, *args):
        value = self.entry_var.get().strip()
        if not value or value == "0":
            self.label_var.set(0)
        else:
            try:
                total = int(value)*20000
                self.label_var.set(total)
                self.controller.set_donation_amount(total)
            except ValueError:
                self.label_var.set(0)
                messagebox.showerror("Error", "Masukkan jumlah pohon yang valid")

    def handle_payment(self):
        try:
            jumlah_pohon = int(self.entry_var.get())
            if jumlah_pohon < 0:
                messagebox.showerror("Error", "Masukkan jumlah yang valid")
                return
            self.controller.show_qris_page()
        except ValueError:
            messagebox.showerror("Error", "Masukkan jumlah pohon yang valid")

class HasilEmisiPage:
    def __init__(self, container, controller, data=None):
        self.controller = controller
        self.data = data or {"emisi": 0, "pohon": 0}

        self.frame = tk.Frame(container, bg="#18656A")
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

        donasi_btn = tk.Button(self.frame, text="DONASI", command=self.controller.show_donasi_page, width=20, height=2, bg="#D9D9D9", fg="#0A2736", font=("Inter", 12))
        donasi_btn.place(relx=0.5, rely=0.725, anchor="center")

        kembali_btn = tk.Button(self.frame, text="KEMBALI", command=self.controller.show_main_menu_page, width=20, height=2, bg="#D9D9D9", fg="#0A2736", font=("Inter", 12))
        kembali_btn.place(relx=0.5, rely=0.825, anchor="center")

class QrisPage:
    def __init__(self, container, controller):
        self.controller = controller
        self.frame = tk.Frame(container, bg="#18656A")
        self.frame.place(x=0, y=0, width=412, height=717)

        label_judul = tk.Label(self.frame, text="BAYAR", fg="#DEE693", bg="#18656A", font=("Inter", 18, "bold"))
        label_judul.place(relx=0.5, rely=0.135, anchor="center")

        label_subjudul = tk.Label(self.frame, text="Scan Barcode di bawah ini", fg="#DEE693", bg="#18656A", font=("Inter", 12, "bold"))
        label_subjudul.place(relx=0.5, rely=0.185, anchor="center")

        try:
            url = "https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi1Pl2OgcZJp0v4sTtS7xvR9n7Tkx1v1i-2uSzMVO-z8zGaIgUDc_N_AoSXY6kvlaLboij5tObKS-_25uVCm8tFteWPFJIpEyBUaFAxjCyYJEQ48_0U_UOZLuQ-bsQw_HDCnsw9n6Lni5Ry/s1600/QR_code_for_mobile_English_Wikipedia.svg.png"
            response = requests.get(url)
            if response.status_code == 200:
                image_data = BytesIO(response.content)
                img = Image.open(image_data)
                img = img.resize((280, 280))
                img = ImageTk.PhotoImage(img)
                label = tk.Label(self.frame, image=img, bg="#E8E8E8", bd=1.5, relief="solid")
                label.image = img
                label.place(relx=0.5, rely=0.43, anchor="center")
            else:
                label = tk.Label(self.frame, text="Gagal memuat gambar QRIS", 
 fg="#DEE693", bg="#18656A", font=("Inter", 12))
                label.place(relx=0.5, rely=0.5, anchor="center")
        except Exception as e:
            label = tk.Label(self.frame, text="Gagal memuat gambar QRIS", fg="#DEE693", bg="#18656A", font=("Inter", 12))
            label.place(relx=0.5, rely=0.5, anchor="center")

        cek_status_btn = tk.Button(self.frame, text="Cek Status Pembayaran", command=self.cek_status, width=20, height=2, bg="#D9D9D9", fg="#0A2736", font=("Inter", 12))
        cek_status_btn.place(relx=0.5, rely=0.725, anchor="center")

        kembali_btn = tk.Button(self.frame, text="KEMBALI", command=self.controller.show_main_menu_page, width=20, height=2, bg="#D9D9D9", fg="#0A2736", font=("Inter", 12))
        kembali_btn.place(relx=0.5, rely=0.825, anchor="center")

    def cek_status(self):
        messagebox.showinfo("Status Pembayaran", "Donasi Berhasil Terkirim🎉🎉🎉")

# CONTROLLER (Logic)
class Controller:
    def __init__(self, root):
        self.model = Model()
        self.view = View(root, self)

    # method navigasi ke jendela tertentu 
    def show_start_page(self):
        self.view.show_page("start")

    def show_login_page(self):
        self.view.show_page("login")

    def show_signup_page(self):
        self.view.show_page("signup")

    def show_main_menu_page(self):
        self.view.show_page("main_menu")

    def show_kalkulator_page(self):
        self.view.show_page("kalkulator")

    def show_transportasi_page(self):
        self.view.show_page("transportasi")

    def show_elektronik_page(self):
        self.view.show_page("elektronik")

    def show_donasi_page(self):
        self.view.show_page("donasi")

    def show_hasil_emisi_page(self, data):
        self.view.show_page("hasil_emisi", data)

    def show_qris_page(self):
        self.view.show_page("qris")

    # User related methods
    def handle_login(self, email, password):
        success, message = self.model.login_user(email, password)
        if success:
            self.show_main_menu_page()
            # Clear fields in login page
            if "login" in self.view.pages:
                self.view.pages["login"].login_email.delete(0, tk.END)
                self.view.pages["login"].login_password.delete(0, tk.END)
        else:
            messagebox.showerror("Error", message)

    def handle_signup(self, nama, email, password):
        success, message = self.model.register_user(nama, email, password)
        if success:
            messagebox.showinfo("Success", message)
            if "signup" in self.view.pages:
                self.view.pages["signup"].entry_nama.delete(0, tk.END)
                self.view.pages["signup"].entry_email.delete(0, tk.END)
                self.view.pages["signup"].entry_password.delete(0, tk.END)
            self.show_start_page()
        else:
            messagebox.showerror("Error", message)

    def logout(self):
        self.model.user_data = None
        self.show_start_page()

    # Carbon calculation methods
    def calculate_transport_emission(self, jenis, jarak, frekuensi):
        try:
            jarak = float(jarak)
            frekuensi = int(frekuensi)
            data = self.model.calculate_transport_emission(jenis, jarak, frekuensi)
            self.show_hasil_emisi_page(data)
        except ValueError:
            messagebox.showerror("Error", "Input tidak valid")

    def calculate_electronic_emission(self, daya, jumlah, durasi, frekuensi):
        try:
            daya = float(daya)
            jumlah = int(jumlah)
            durasi = float(durasi)
            frekuensi = int(frekuensi)
            data = self.model.calculate_electronic_emission(daya, jumlah, durasi, frekuensi)
            self.show_hasil_emisi_page(data)
        except ValueError:
            messagebox.showerror("Error", "Input tidak valid")

    # Donation methods
    def set_donation_amount(self, amount):
        self.model.donation_data = {"amount": amount}

    def process_payment(self):
        messagebox.showinfo("Status Pembayaran", "Donasi Berhasil Terkirim🎉🎉🎉")

# APPLICATION ENTRY POINT

if __name__ == "__main__":
    root = tk.Tk()
    app = Controller(root)
    root.mainloop()
