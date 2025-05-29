from tkinter import *
from tkinter import messagebox
import math
from PIL import ImageTk, Image

labelKeteranganEmisi = None
labelKeteranganPohon = None

def main_menu(container, show_page):

    frameFitur = Frame(container, bg="#DEE693")
    frameFitur.place(relx=0, rely=0, relwidth=1, relheight=1)

    kembaliKePageAwal = Button(frameFitur, text="<<<<", command=lambda: show_page(), width=5, height=2, bg="#8FC07C", fg="#0A2736", font=("Inter", 12), anchor="center")
    kembaliKePageAwal.place(relx=0.05, rely=0.035)

    tomboKalkulator = Button(frameFitur, text="KALKULATOR KARBON", command=lambda: show_page(kePageSumberEmisi), width=20, height=2, bg="#8FC07C", fg="#0A2736", font=("Inter", 12))
    tomboKalkulator.place(relx=0.3, rely=0.45, anchor="center")

    tombolDonasi = Button(frameFitur, text="DONASI", command=lambda: show_page(kePageDonasi), width=20, height=2, bg="#8FC07C", fg="#0A2736", font=("Inter", 12))
    tombolDonasi.place(relx=0.7, rely=0.6, anchor="center")

    tomboKeluar = Button(frameFitur, text="KELUAR", command=keluar, width=20, height=2, bg="#8FC07C", fg="#0A2736", font=("Inter", 12))
    tomboKeluar.place(relx=0.3, rely=0.75, anchor="center")

    # tomboKeluar = Button(frameFitur, text="Keluar", command=keluar, width=5, height=2, bg="#8FC07C", fg="#0A2736", font=("Inter", 12), anchor="center")
    # tomboKeluar.place(relx=0.815, rely=0.035)

    return frameFitur

def kategori_kalkulator_karbon(container, show_page):

    frameSumberEmisi = Frame(container, bg="#436651")
    frameSumberEmisi.place(relx=0, rely=0, relwidth=1, relheight=1)

    label = Label(frameSumberEmisi, text="KALKULATOR\nKARBON", fg="#DEE693", bg="#436651", font=("Inter", 18, "bold"), justify="right", anchor="e")
    label.place(relx=0.5, rely=0.1)

    kembaliKePageFitur = Button(frameSumberEmisi, text="<<<<", command=lambda: show_page(kePageFitur), width=5, height=2, bg="#DEE693", fg="#0A2736", font=("Inter", 12), anchor="center")
    kembaliKePageFitur.place(relx=0.05, rely=0.035)

    tombolKendaraan = Button(frameSumberEmisi, text="Kendaraan", width=20, height=2, bg="#DEE693", fg="#0A2736", font=("Inter", 12))
    tombolKendaraan.place(relx=0.3, rely=0.45, anchor="center")

    tombolElektronik = Button(frameSumberEmisi, text="Elektronik", command=lambda: show_page(kePageElektronik), width=20, height=2, bg="#DEE693", fg="#0A2736", font=("Inter", 12))
    tombolElektronik.place(relx=0.7, rely=0.6, anchor="center")

    return frameSumberEmisi

def pageElektronik(container, show_page):

    frameElektronik = Frame(container)
    frameElektronik.place(relx=0, rely=0, relwidth=1, relheight=1)

    # kembaliKePageSumberEmisi = Button(frameElektronik, text="<<<<", command=lambda: show_page(kePageFitur), width=5, height=2, bg="#D9D9D9", fg="#0A2736", font=("Inter", 12), anchor="center")
    # kembaliKePageSumberEmisi.place(relx=0.05, rely=0.035)

    label = Label(frameElektronik, text="ELEKTRONIK", fg="#0A2736", font=("Inter", 18, "bold"), anchor="center")
    label.place(relx=0.5, rely=0.135, anchor="center")

    global entryDayaPerangkat, entryJumlahPerangkat, entryDurasi, entryFrekuensi

    labelDayaPerangkat = Label(frameElektronik, text="Daya Perangkat (watt)", fg="#0A2736", font=("Inter", 12, "bold"), justify="left")
    labelDayaPerangkat.place(relx=0.25, rely=0.250)

    entryDayaPerangkat = Entry(frameElektronik, bg="#D9D9D9", fg="#0A2736", font=("Inter", 12))
    entryDayaPerangkat.place(relx=0.5, rely=0.325, anchor="center", width=200, height=30)

    labelJumlahPerangkat = Label(frameElektronik, text="Jumlah Perangkat", fg="#0A2736", font=("Inter", 12, "bold"), justify="left", anchor="w")
    labelJumlahPerangkat.place(relx=0.25, rely=0.350)

    entryJumlahPerangkat = Entry(frameElektronik, bg="#D9D9D9", fg="#0A2736", font=("Inter", 12))
    entryJumlahPerangkat.place(relx=0.5, rely=0.425, anchor="center", width=200, height=30)

    labelDurasi = Label(frameElektronik, text="Durasi (jam)", fg="#0A2736", font=("Inter", 12, "bold"), justify="left", anchor="w")
    labelDurasi.place(relx=0.25, rely=0.450)

    entryDurasi = Entry(frameElektronik, bg="#D9D9D9", fg="#0A2736", font=("Inter", 12))
    entryDurasi.place(relx=0.5, rely=0.525, anchor="center", width=200, height=30)

    labelFrekuensi = Label(frameElektronik, text="Frekuensi (Hari)", fg="#0A2736", font=("Inter", 12, "bold"), justify="left", anchor="w")
    labelFrekuensi.place(relx=0.25, rely=0.550)

    entryFrekuensi = Entry(frameElektronik, bg="#D9D9D9", fg="#0A2736", font=("Inter", 12))
    entryFrekuensi.place(relx=0.5, rely=0.625, anchor="center", width=200, height=30)

    tombolHitungEmisi = Button(frameElektronik, text="Hitung", command=lambda: [total_emisi_elektronika(), show_page(kePagePenghitunganEmisi)], width=20, height=2, bg="#D9D9D9", fg="#0A2736", font=("Inter", 12))
    tombolHitungEmisi.place(relx=0.5, rely=0.725, anchor="center")

    kembaliKePageFitur = Button(frameElektronik, text="KEMBALI", command=lambda: show_page(kePageFitur), width=20, height=2, bg="#D9D9D9", fg="#0A2736", font=("Inter", 12))
    kembaliKePageFitur.place(relx=0.5, rely=0.825, anchor="center")


    return frameElektronik

def pagePenghitunganEmisi(container, show_page):

    # Frame untuk Halaman 2
    framePerhitunganEmisi = Frame(container, bg="#18656A")
    framePerhitunganEmisi.place(relx=0, rely=0, relwidth=1, relheight=1)

    global labelKeteranganEmisi, labelKeteranganPohon

    labelNarasiEmisi = Label(framePerhitunganEmisi, text="EMISI\nKarbon Anda:", bg="#18656A", fg="#DEE693", font=("Inter", 18, "bold"), justify="left")
    labelNarasiEmisi.place(relx=0.5, rely=0.175, anchor="e")

    labelKeteranganEmisi = Label(framePerhitunganEmisi, text="Masukkan Input", bg="#DEE693", fg="#0A2736", font=("Inter", 18, "bold"), justify="left", padx=5, pady=5)
    labelKeteranganEmisi.place(relx=0.1, rely=0.26, width=220, height=45, anchor="w")

    labelSatuanEmisi = Label(framePerhitunganEmisi, text="KG", bg="#DEE693", fg="#0A2736", font=("Inter", 18, "bold"), justify="right")
    labelSatuanEmisi.place(relx=0.9, rely=0.26, width=85, height=45, anchor="e")

    labelNarasiPohon = Label(framePerhitunganEmisi, text="Membutuhkan:", bg="#18656A", fg="#DEE693", font=("Inter", 18, "bold"), justify="left")
    labelNarasiPohon.place(relx=0.535, rely=0.435, anchor="e")

    labelKeteranganPohon = Label(framePerhitunganEmisi, text="-", bg="#DEE693", fg="#0A2736", font=("Inter", 18, "bold"), justify="left", padx=5, pady=5)
    labelKeteranganPohon.place(relx=0.1, rely=0.5, width=220, height=45, anchor="w")

    labelSatuanEmisi = Label(framePerhitunganEmisi, text="Pohon", bg="#DEE693", fg="#0A2736", font=("Inter", 18, "bold"), justify="right")
    labelSatuanEmisi.place(relx=0.9, rely=0.5, width=85, height=45, anchor="e")

    tombolDonasi = Button(framePerhitunganEmisi, text="DONASI", command=lambda: show_page(kePageDonasi), width=20, height=2, bg="#D9D9D9", fg="#0A2736", font=("Inter", 12))
    tombolDonasi.place(relx=0.5, rely=0.725, anchor="center")

    kembaliKePageFitur = Button(framePerhitunganEmisi, text="KEMBALI", command=lambda: show_page(kePageFitur), width=20, height=2, bg="#D9D9D9", fg="#0A2736", font=("Inter", 12))
    kembaliKePageFitur.place(relx=0.5, rely=0.825, anchor="center")

    return framePerhitunganEmisi

def donasi_pohon(container, show_page):

    frameDonasi = Frame(container, bg="#436651")
    frameDonasi.place(relx=0, rely=0, relwidth=1, relheight=1)

    global entryJumlahPohon, labelJumlahDonasi, variabelEntry, variabelLabel

    labelJudulDonasi = Label(frameDonasi, text="DONASI", fg="#DEE693", bg="#436651", font=("Inter", 18, "bold"))
    labelJudulDonasi.place(relx=0.5, rely=0.135, anchor="center")

    labelHargaPohon = Label(frameDonasi, text="1 Pohon = Rp. 20.000", fg="#0A2736", bg="#DEE693", font=("Inter", 12, "bold"), justify="left")
    labelHargaPohon.place(relx=0.5, rely=0.25, width=250, height=50, anchor="center")

    labelJumlahPohon = Label(frameDonasi, text="Pohon", fg="#0A2736", bg="#DEE693", font=("Inter", 12, "bold"))
    labelJumlahPohon.place(relx=0.523, rely=0.35, width=115, height=50, anchor="w")

    variabelEntry = IntVar()
    variabelLabel = IntVar()

    variabelEntry.trace_add("write", hitung_donasi)

    entryJumlahPohon = Entry(frameDonasi, justify="center", textvariable=variabelEntry, bg="#DEE693", fg="#0A2736", font=("Inter", 12, "bold"))
    entryJumlahPohon.place(relx=0.187, rely=0.35, relwidth=0.1, anchor="w", width=80, height=50)

    labelRupiah = Label(frameDonasi, text="Rp.", fg="#0A2736", bg="#DEE693", font=("Inter", 12, "bold"), anchor="center")
    labelRupiah.place(relx=0.187, rely=0.45, relwidth=0.1, anchor="w", width=80, height=50)

    labelJumlahDonasi = Label(frameDonasi, textvariable=variabelLabel, fg="#0A2736", bg="#DEE693", font=("Inter", 12, "bold"),  anchor="center")
    labelJumlahDonasi.place(relx=0.523, rely=0.45, width=115, height=50, anchor="w")

    tombolDonasi = Button(frameDonasi, text="BAYAR", command=lambda: show_page(kePageQris), width=20, height=2, bg="#D9D9D9", fg="#0A2736", font=("Inter", 12))
    tombolDonasi.place(relx=0.5, rely=0.725, anchor="center")

    kembaliKePageFitur = Button(frameDonasi, text="KEMBALI", command=lambda: show_page(kePageFitur), width=20, height=2, bg="#D9D9D9", fg="#0A2736", font=("Inter", 12))
    kembaliKePageFitur.place(relx=0.5, rely=0.825, anchor="center")

    return frameDonasi

def pageQris(container, show_page):

    frameQris = Frame(container, bg="#18656A")
    frameQris.place(relx=0, rely=0, relwidth=1, relheight=1)

    labelJudulBayar = Label(frameQris, text="BAYAR", fg="#DEE693", bg="#18656A", font=("Inter", 18, "bold"))
    labelJudulBayar.place(relx=0.5, rely=0.135, anchor="center")
    labelJudulDonasi = Label(frameQris, text="Scan Barcode di bawah ini", fg="#DEE693", bg="#18656A", font=("Inter", 12, "bold"))
    labelJudulDonasi.place(relx=0.5, rely=0.185, anchor="center")

    def cekStatus():
        messagebox.showinfo("Status Pembayaran", "Donasi Berhasil Terkirim🎉🎉🎉")

    try:
        img = Image.open("qris_barcode.png")
        img = img.resize((280, 280))
        img = ImageTk.PhotoImage(img)
        label = Label(frameQris, image=img, bg="#18656A", bd=1.5, relief="solid")
        label.image = img
        label.place(relx=0.5, rely=0.43, anchor="center")

    except FileNotFoundError:

        label = Label(frameQris, text="Gambar QRIS tidak ditemukan\nPastikan gambar file berada di repositori yang sama", fg="#DEE693", bg="#18656A", font=("Arial", 12))
        label.place(relx=0.5, rely=0.5, anchor="center")

    tombolCekStatus = Button(frameQris, text="Cek Status Pembayaran", command=cekStatus, width=20, height=2, bg="#D9D9D9", fg="#0A2736", font=("Inter", 12))
    tombolCekStatus.place(relx=0.5, rely=0.725, anchor="center")

    kembaliKePageDonasi = Button(frameQris, text="KEMBALI", command=lambda: show_page(kePageFitur), width=20, height=2, bg="#D9D9D9", fg="#0A2736", font=("Inter", 12))
    kembaliKePageDonasi.place(relx=0.5, rely=0.825, anchor="center")

    return frameQris

def total_emisi_elektronika():

    try:
        daya = float(entryDayaPerangkat.get())
        jumlah = int(entryJumlahPerangkat.get())
        durasi = float(entryDurasi.get())
        frekuensi = int(entryFrekuensi.get())

        total_emisi_elektronika = (daya * jumlah * durasi * frekuensi) / 1000
        labelKeteranganEmisi.config(text=f"{total_emisi_elektronika:.2f}")

        def total_pohon():
            pohon = math.ceil(total_emisi_elektronika / 25)
            return labelKeteranganPohon.config(text=f"{pohon:.0f}")
        total_pohon()

    except ValueError:
        labelKeteranganEmisi.config(text="Input tidak valid")
        labelKeteranganPohon.config(text="-")

def hitung_donasi(*args):
    try:
        inputPengguna = entryJumlahPohon.get()
        if inputPengguna.strip() == "":
            variabelLabel.set(0)
        else:
            total_donasi = int(inputPengguna) * 20000
            variabelLabel.set(total_donasi)
    except ValueError:
        variabelLabel.set(0)

def main():

    global window

    window = Tk()
    window.title("Ksatria Taru")

    screenWidth = window.winfo_screenwidth()
    screenHeight = window.winfo_screenheight()
    width, height = 400, 640
    mainWidth = (screenWidth - width) // 2
    mainHeight = ((screenHeight - height) // 2) - (round(screenHeight * 0.05))
    window.geometry(f"{width}x{height}+{mainWidth}+{mainHeight}")
    window.resizable(False, False)

    container = Frame(window)
    container.place(relx=0, rely=0, relwidth=1, relheight=1)

    def show_page(frame):
        frame.tkraise()

    global kePageFitur, kePageSumberEmisi, kePageElektronik, kePagePenghitunganEmisi, kePageDonasi, kePageQris
    kePageFitur = main_menu(container, show_page)
    kePageSumberEmisi = kategori_kalkulator_karbon(container, show_page)
    kePageElektronik = pageElektronik(container, show_page)
    kePagePenghitunganEmisi = pagePenghitunganEmisi(container, show_page)
    kePageDonasi = donasi_pohon(container, show_page)
    kePageQris = pageQris(container, show_page)

    show_page(kePageFitur)

    window.mainloop()

def keluar():
    window.destroy() 

if __name__ == "__main__":

    main()
