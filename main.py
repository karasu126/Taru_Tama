import tkinter as tk
import os
import json

class KsatriaTaruApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Ksatria Taru")
        self.root.geometry("412x717")
        self.root.resizable(False, False)

        if not os.path.exists("data_akun"):
            os.makedirs("data_akun")

        self.create_frames()
        self.create_start_screen()
        self.create_login_screen()
        self.create_signup_screen()
        self.create_main_menu()
        self.create_calculator_menu()
        self.show_frame(self.start_frame)

    def create_frames(self):
        self.start_frame = tk.Frame(self.root, bg="#DEE693")
        self.login_frame = tk.Frame(self.root, bg="#CADFC4")
        self.signup_frame = tk.Frame(self.root, bg="#436651")
        self.main_menu_frame = tk.Frame(self.root, bg="#DEE693")
        self.calculator_menu_frame = tk.Frame(self.root, bg="#436651")

        for frame in [self.start_frame, self.login_frame, self.signup_frame, self.main_menu_frame, self.calculator_menu_frame]:
            frame.place(x=0, y=0, width=412, height=717)

    def create_start_screen(self):
        tk.Label(self.start_frame, text="Selamat\nDatang,\nKsatria Taru!", 
                bg="#DEE693", font=("Inter", 17), justify="center").place(relx=0.5, y=80, anchor="center")

        tk.Canvas(self.start_frame, width=50, height=80, bg="#436651", highlightthickness=0).place(relx=0.5, y=200, anchor="center")

        tk.Button(self.start_frame, text="Login", bg="white", command=self.show_login,
                relief="flat", font=("Inter", 10, "bold")).place(relx=0.5, rely=0.6, anchor="center", width=150, height=35)

        tk.Button(self.start_frame, text="Sign Up", bg="white", command=self.show_signup,
                relief="flat", font=("Inter", 10, "bold")).place(relx=0.5, rely=0.67, anchor="center", width=150, height=35)

    def create_login_screen(self):
        header = tk.Frame(self.login_frame, bg="#2f4f3c", height=100)
        header.pack(fill="x")

        tk.Button(header, text="<", command=self.show_start, bg="#2f4f3c", fg="white", relief="flat").place(x=5, y=5)

        form = tk.Frame(self.login_frame, bg="#8ba98f")
        form.pack(fill="both", expand=True)

        tk.Label(form, text="Login", bg="#8ba98f", font=("Inter", 12, "bold")).pack(pady=20)

        tk.Label(form, text="Alamat Email:", bg="#8ba98f").pack(anchor="w", padx=20)
        self.login_email = tk.Entry(form)
        self.login_email.pack(padx=20, fill="x")

        tk.Label(form, text="Password:", bg="#8ba98f").pack(anchor="w", padx=20, pady=(10, 0))
        self.login_password = tk.Entry(form, show="*")
        self.login_password.pack(padx=20, fill="x")

        tk.Button(form, text="Login", bg="white", font=("Inter", 10, "bold"),
                  command=self.check_login).pack(pady=10, ipadx=10, ipady=2)

        tk.Label(form, text="Belum punya akun?", bg="#8ba98f").pack(side="left", padx=(30, 2), pady=10)
        tk.Button(form, text="Sign Up", bg="#8ba98f", fg="blue", font=("Inter", 9, "bold"),
                  relief="flat", command=self.show_signup).pack(side="left")

    def create_signup_screen(self):
        header = tk.Frame(self.signup_frame, bg="#8ba98f", height=100)
        header.pack(fill="x")

        tk.Button(header, text="<", command=self.show_start, bg="#8ba98f", fg="black", relief="flat").place(x=5, y=5)

        form = tk.Frame(self.signup_frame, bg="#2f4f3c")
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

        tk.Button(form, text="Sign Up", bg="white", font=("Inter", 10, "bold"),
                  command=self.save_signup_data).pack(pady=10, ipadx=10, ipady=2)

        tk.Label(form, text="Sudah punya akun?", bg="#2f4f3c", fg="white").pack(side="left", padx=(30, 2), pady=10)
        tk.Button(form, text="Login", bg="#2f4f3c", fg="lightblue", font=("Inter", 9, "bold"),
                  relief="flat", command=self.show_login).pack(side="left")

    def create_main_menu(self):
        content = tk.Frame(self.main_menu_frame, bg="#DEE693")
        content.pack(fill="both", expand=True)
        tk.Button(content, text="<", command=self.show_start, bg="#DEE693", fg="black", relief="flat").place(x=5, y=5)

        btn1 = tk.Button(content, text="Kalkulator Karbon", width=20, height=2, bg="#8FC07C", fg="#000000", font=("Arial", 12),
                         command=self.show_calculator_menu)
        btn1.place(relx=0.3, rely=0.3, anchor="center")

        btn2 = tk.Button(content, text="Donasi", width=20, height=2, bg="#8FC07C", fg="#000000", font=("Arial", 12))
        btn2.place(relx=0.7, rely=0.55, anchor="center")

    def create_calculator_menu(self):
        content = tk.Frame(self.calculator_menu_frame, bg="#436651")
        content.pack(fill="both", expand=True)
        tk.Button(content, text="<", command=self.show_main_menu, bg="#436651", fg="black", relief="flat").place(x=5, y=5)

        btn1 = tk.Button(content, text="Kendaraan", width=20, height=2, bg="#DEE693", fg="#000000", font=("Arial", 12))
        btn1.place(relx=0.3, rely=0.3, anchor="center")

        btn2 = tk.Button(content, text="Elektronika", width=20, height=2, bg="#DEE693", fg="#000000", font=("Arial", 12))
        btn2.place(relx=0.7, rely=0.55, anchor="center")

    def save_signup_data(self):
        nama = self.entry_nama.get()
        email = self.entry_email.get()
        password = self.entry_password.get()

        if not nama or not email or not password:
            print("Semua field harus diisi!")
            return

        data = {
            "nama": nama,
            "email": email,
            "password": password
        }

        filename = os.path.join("data_akun", f"{email.replace('@','_at_')}.json")
        with open(filename, "w") as f:
            json.dump(data, f, indent=4)

        print(f"Akun untuk {email} telah disimpan.")
        self.entry_nama.delete(0, tk.END)
        self.entry_email.delete(0, tk.END)
        self.entry_password.delete(0, tk.END)

        self.show_start()

    def check_login(self):
        email = self.login_email.get()
        password = self.login_password.get()

        filename = os.path.join("data_akun", f"{email.replace('@','_at_')}.json")
        if os.path.exists(filename):
            with open(filename, "r") as f:
                data = json.load(f)
                if data["password"] == password:
                    self.login_email.delete(0, tk.END)
                    self.login_password.delete(0, tk.END)
                    self.show_main_menu()
                else:
                    print("Password salah!")
        else:
            print("Email tidak ditemukan!")

    def show_frame(self, frame):
        frame.tkraise()

    def show_start(self):
        self.show_frame(self.start_frame)

    def show_login(self):
        self.show_frame(self.login_frame)

    def show_signup(self):
        self.show_frame(self.signup_frame)

    def show_main_menu(self):
        self.show_frame(self.main_menu_frame)

    def show_calculator_menu(self):
        self.show_frame(self.calculator_menu_frame)


if __name__ == "__main__":
    root = tk.Tk()
    app = KsatriaTaruApp(root)
    root.mainloop()
