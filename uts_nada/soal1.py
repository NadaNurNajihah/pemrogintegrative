#Nama		    : Nada Nur Najihah
#NIM		    : 239902342
#kelas			: KOM C (PMM)
#Mata Kuliah	: Pemrograman Integrative
####### UTS #########

import datetime

def hitung_pembagian(bilangan):
    # Mendapatkan jumlah hari dalam tahun ini
    tahun_ini = datetime.datetime.now().year
    if tahun_ini % 4 == 0 and (tahun_ini % 100 != 0 or tahun_ini % 400 == 0):
        jumlah_hari = 366  # Tahun kabisat
    else:
        jumlah_hari = 365  # Bukan tahun kabisat

    # Melakukan pembagian
    hasil_pembagian = bilangan / jumlah_hari

    # Menampilkan hasil dengan 11 angka di belakang koma (jika ada)
    print("Hasil pembagian:", format(hasil_pembagian, ".11f"))

def main():
    try:
        bilangan = int(input("Masukkan bilangan bulat: "))
        hitung_pembagian(bilangan)
    except ValueError:
        print("Input tidak valid. Masukkan bilangan bulat.")

if __name__ == "__main__":
    main()
