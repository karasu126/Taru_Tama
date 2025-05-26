from tkinter import *

labelKeteranganEmisi = None
labelKeteranganPohon = None

def pageFitur(container, show_page):

    # Frame untuk Halaman 1
    frameFitur = Frame(container, bg="#DEE693")
    frameFitur.place(relx=0, rely=0, relwidth=1, relheight=1)

    kembaliKePageAwal = Button(frameFitur, text="<<<<", command=lambda: show_page(), width=5, height=2, bg="#8FC07C", fg="#000000", font=("Inter", 12), anchor="center")
    kembaliKePageAwal.place(relx=0.05, rely=0.035)

    # Tombol untuk fitur kalkulator
    tomboKalkulator = Button(frameFitur, text="KALKULATOR KARBON", command=lambda: show_page(kePageSumberEmisi), width=20, height=2, bg="#8FC07C", fg="#0A2736", font=("Inter", 12))
    tomboKalkulator.place(relx=0.3, rely=0.45, anchor="center")

    # Tombol untuk fitur donasi
    tombolDonasi = Button(frameFitur, text="DONASI", width=20, height=2, bg="#8FC07C", fg="#0A2736", font=("Inter", 12))
    tombolDonasi.place(relx=0.7, rely=0.6, anchor="center")

    return frameFitur

def pageSumberEmisi(container, show_page):

    # Frame untuk Halaman 2
    frameSumberEmisi = Frame(container, bg="#436651")
    frameSumberEmisi.place(relx=0, rely=0, relwidth=1, relheight=1)

    # Label untuk judul halaman
    label = Label(frameSumberEmisi, text="KALKULATOR\nKARBON", fg="#0A2736", bg="#436651", font=("Inter", 18, "bold"), justify="right", anchor="e")
    label.place(relx=0.5, rely=0.1)

    # Tombol untuk kembali ke halaman pilih_fitur
    kembaliKePageFitur = Button(frameSumberEmisi, text="<<<<", command=lambda: show_page(kePageFitur), width=5, height=2, bg="#DEE693", fg="#000000", font=("Inter", 12), anchor="center")
    kembaliKePageFitur.place(relx=0.05, rely=0.035)

    # Tombol untuk kendaraan
    tombolKendaraan = Button(frameSumberEmisi, text="Kendaraan", width=20, height=2, bg="#DEE693", fg="#0A2736", font=("Inter", 12))
    tombolKendaraan.place(relx=0.3, rely=0.45, anchor="center")

    # Tombol untuk elektronik
    tombolElektronik = Button(frameSumberEmisi, text="Elektronik", command=lambda: show_page(kePageElektronik), width=20, height=2, bg="#DEE693", fg="#0A2736", font=("Inter", 12))
    tombolElektronik.place(relx=0.7, rely=0.6, anchor="center")

    return frameSumberEmisi

def pageElektronik(container, show_page):

    # Frame untuk Halaman 2
    frameElektronik = Frame(container)
    frameElektronik.place(relx=0, rely=0, relwidth=1, relheight=1)

    # Tombol untuk kembali ke halaman sumber emisi
    kembaliKePageSumberEmisi = Button(frameElektronik, text="<<<<", command=lambda: show_page(kePageSumberEmisi), width=5, height=2, bg="#D9D9D9", fg="#000000", font=("Inter", 12), anchor="center")
    kembaliKePageSumberEmisi.place(relx=0.05, rely=0.035)

    # Label untuk judul halaman
    label = Label(frameElektronik, text="ELEKTRONIK", fg="#0A2736", font=("Inter", 18, "bold"))
    label.place(relx=0.5, rely=0.135, anchor="center")

    global entryDayaPerangkat, entryJumlahPerangkat, entryDurasi, entryFrekuensi

    # Label untuk daya perangkat
    labelDayaPerangkat = Label(frameElektronik, text="Daya Perangkat (watt)", fg="#0A2736", font=("Inter", 12, "bold"), justify="left")
    labelDayaPerangkat.place(relx=0.25, rely=0.250)

    # Entry untuk daya perangkat
    entryDayaPerangkat = Entry(frameElektronik, bg="#D9D9D9", fg="#000000", font=("Inter", 12))
    entryDayaPerangkat.place(relx=0.5, rely=0.325, anchor="center", width=200, height=30)

    # Label untuk jumlah perangkat
    labelJumlahPerangkat = Label(frameElektronik, text="Jumlah Perangkat", fg="#0A2736", font=("Inter", 12, "bold"), justify="left", anchor="w")
    labelJumlahPerangkat.place(relx=0.25, rely=0.350)

    # Entry untuk jumlah perangkat
    entryJumlahPerangkat = Entry(frameElektronik, bg="#D9D9D9", fg="#000000", font=("Inter", 12))
    entryJumlahPerangkat.place(relx=0.5, rely=0.425, anchor="center", width=200, height=30)

    # Label untuk durasi penggunaan perangkat
    labelDurasi = Label(frameElektronik, text="Durasi (jam)", fg="#0A2736", font=("Inter", 12, "bold"), justify="left", anchor="w")
    labelDurasi.place(relx=0.25, rely=0.450)

    # Entry untuk durasi penggunaan perangkat
    entryDurasi = Entry(frameElektronik, bg="#D9D9D9", fg="#000000", font=("Inter", 12))
    entryDurasi.place(relx=0.5, rely=0.525, anchor="center", width=200, height=30)

    # Label untuk frekuensi penggunaan perangkat
    labelFrekuensi = Label(frameElektronik, text="Frekuensi (Hari)", fg="#0A2736", font=("Inter", 12, "bold"), justify="left", anchor="w")
    labelFrekuensi.place(relx=0.25, rely=0.550)

    # Entry untuk frekuensi penggunaan perangkat
    entryFrekuensi = Entry(frameElektronik, bg="#D9D9D9", fg="#000000", font=("Inter", 12))
    entryFrekuensi.place(relx=0.5, rely=0.625, anchor="center", width=200, height=30)

    # Tombol untuk fitur melakukan perhitungan
    tombolHitungEmisi = Button(frameElektronik, text="Hitung", command=lambda: [hitung_emisi(), show_page(kePagePenghitunganEmisi)], width=20, height=2, bg="#D9D9D9", fg="#000000", font=("Inter", 12))
    tombolHitungEmisi.place(relx=0.5, rely=0.725, anchor="center")

    return frameElektronik

def pagePenghitunganEmisi(container, show_page):

    global labelKeteranganEmisi, labelKeteranganPohon

    # Frame untuk Halaman 2
    framePerhitunganEmisi = Frame(container, bg="#18656A")
    framePerhitunganEmisi.place(relx=0, rely=0, relwidth=1, relheight=1)

    # Label teks jumlah emisi pengguna
    labelNarasiEmisi = Label(framePerhitunganEmisi, text="EMISI\nKarbon Anda:", bg="#18656A", fg="#DEE693", font=("Inter", 18, "bold"), justify="left")
    labelNarasiEmisi.place(relx=0.5, rely=0.175, anchor="e")

    # Label untuk menampilkan hasil emisi
    labelKeteranganEmisi = Label(framePerhitunganEmisi, text="", bg="#DEE693", fg="#181818", font=("Inter", 18, "bold"), justify="left", padx=5, pady=5)
    labelKeteranganEmisi.place(relx=0.1, rely=0.26, width=210, anchor="w")

    # Label untuk menampilkan hasil emisi
    labelSatuanEmisi = Label(framePerhitunganEmisi, text="KG", bg="#18656A", fg="#DEE693", font=("Inter", 18, "bold"), justify="right", padx=5, pady=5)
    labelSatuanEmisi.place(relx=0.9, rely=0.26, width=50, anchor="e")

    # Label teks jumlah emisi pengguna
    
    labelNarasiPohon = Label(framePerhitunganEmisi, text="Membutuhkan:", bg="#18656A", fg="#DEE693", font=("Inter", 18, "bold"), justify="left")
    labelNarasiPohon.place(relx=0.535, rely=0.415, anchor="e")

    # Label untuk menampilkan hasil emisi
    labelKeteranganPohon = Label(framePerhitunganEmisi, text="", bg="#DEE693", fg="#181818", font=("Inter", 18, "bold"), justify="left", padx=5, pady=5)
    labelKeteranganPohon.place(relx=0.1, rely=0.5, width=100, anchor="w")

    # Label untuk menampilkan hasil emisi
    labelSatuanEmisi = Label(framePerhitunganEmisi, text="Pohon", bg="#18656A", fg="#DEE693", font=("Inter", 18, "bold"), justify="right", padx=5, pady=5)
    labelSatuanEmisi.place(relx=0.9, rely=0.5, width=75, anchor="e")

    # Tombol untuk donasi
    tombolDonasi = Button(framePerhitunganEmisi, text="DONASI", width=20, height=2, bg="#D9D9D9", fg="#000000", font=("Inter", 12))
    tombolDonasi.place(relx=0.5, rely=0.7, anchor="center")

    # Tombol untuk kembali ke halaman elektronik
    kembaliKePageFitur = Button(framePerhitunganEmisi, text="KEMBALI", command=lambda: show_page(kePageFitur), width=20, height=2, bg="#D9D9D9", fg="#000000", font=("Inter", 12))
    kembaliKePageFitur.place(relx=0.5, rely=0.8, anchor="center")

    return framePerhitunganEmisi

def hitung_emisi():

    try:
        daya = float(entryDayaPerangkat.get())
        jumlah = int(entryJumlahPerangkat.get())
        durasi = float(entryDurasi.get())
        frekuensi = int(entryFrekuensi.get())

        # Fungsi untuk menghitung emisi berdasarkan input pengguna
        emisi = (daya * jumlah * durasi * frekuensi) / 1000
        labelKeteranganEmisi.config(text=f"{emisi:.2f}")
        labelKeteranganEmisi.place(width=100)

        pohon = emisi / 25
        labelKeteranganPohon.config(text=f"{pohon:.2f}")

    except ValueError:
        labelKeteranganEmisi.config(text="Input tidak valid")
        labelKeteranganPohon.config(text="Error")

def main():

    # Inisialisasi jendela utama
    window = Tk()
    window.title("Taru Tama")

    # Mengatur ukuran dan posisi jendela
    screenWidth = window.winfo_screenwidth()
    screenHeight = window.winfo_screenheight()
    width, height = 400, 640
    mainWidth = (screenWidth - width) // 2
    mainHeight = ((screenHeight - height) // 2) - (round(screenHeight * 0.05))
    window.geometry(f"{width}x{height}+{mainWidth}+{mainHeight}")
    window.resizable(False, False)

    # Kontainer utama untuk semua frame
    container = Frame(window)
    container.place(relx=0, rely=0, relwidth=1, relheight=1)

    # Fungsi untuk pindah halaman
    def show_page(frame):
        frame.tkraise()

    # Buat kedua halaman
    global kePageFitur, kePageSumberEmisi, kePageElektronik, kePagePenghitunganEmisi
    kePageFitur = pageFitur(container, show_page)
    kePageSumberEmisi = pageSumberEmisi(container, show_page)
    kePageElektronik = pageElektronik(container, show_page)
    kePagePenghitunganEmisi = pagePenghitunganEmisi(container, show_page)

    # Tampilkan Halaman 1 pertama kali
    show_page(kePageFitur)

    window.mainloop()

if __name__ == "__main__":
    main()
