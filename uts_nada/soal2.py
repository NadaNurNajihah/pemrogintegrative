#Nama		    : Nada Nur Najihah
#NIM		    : 239902342
#kelas			: KOM C (PMM)
#Mata Kuliah	: Pemrograman Integrative
####### UTS #########

def hitung_perkalian(angka):
    # Inisialisasi hasil
    hasil = 1

    # Perkalian semua nilai dari 1 hingga angka
    for i in range(1, angka + 1):
        hasil *= i

    return hasil

def main():
    try:
        angka = int(input("Masukkan angka (tanggal tes hari ini): "))
        if angka < 0:
            print("Masukkan angka positif.")
        else:
            hasil_perkalian = hitung_perkalian(angka)
            print("Hasil perkalian dari 1 hingga", angka, "adalah:", hasil_perkalian)
    except ValueError:
        print("Input tidak valid. Masukkan angka integer.")

if __name__ == "__main__":
    main()
