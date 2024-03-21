#Nama		    : Nada Nur Najihah
#NIM		    : 239902342
#kelas			: KOM C (PMM)
#Mata Kuliah	: Pemrograman Integrative

def main():
    # Inisialisasi list untuk menyimpan nilai
    nilai = []

    # Minta pengguna untuk memasukkan nilai
    while True:
        try:
            input_nilai = int(input("Masukkan nilai (-1 untuk selesai): "))
            if input_nilai == -1:
                break
            nilai.append(input_nilai)
        except ValueError:
            print("Masukkan angka yang valid.")

    # Hitung rata-rata
    if nilai:
        rata_rata = sum(nilai) / len(nilai)
    else:
        rata_rata = 0

    # Cetak rata-rata
    print("Rata-rata nilai adalah:", int(rata_rata))

    # Cetak nilai sesuai urutan
    print("Nilai sesuai urutan:")
    for n in nilai:
        print(n)

if __name__ == "__main__":
    main()
