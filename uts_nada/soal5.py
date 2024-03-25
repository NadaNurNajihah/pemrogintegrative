#Nama		    : Nada Nur Najihah
#NIM		    : 239902342
#kelas			: KOM C (PMM)
#Mata Kuliah	: Pemrograman Integrative
####### UTS #########


def baca_dan_cetak(file_name):
    try:
        # Membuka file untuk membaca
        with open(file_name, 'r') as file:
            # Membaca baris dari file
            lines = file.readlines()

            # Menginisialisasi daftar untuk menyimpan angka-angka
            angka_list = []

            # Mengambil bilangan bulat dari setiap baris dan menambahkannya ke daftar
            for line in lines:
                try:
                    angka = int(line.strip())  # Menghilangkan whitespace dan mengonversi ke integer
                    angka_list.append(angka)
                except ValueError:
                    print(f"Ignoring non-integer value in file: {line}")

            # Mengubah daftar angka menjadi string dengan pemisah koma setiap tiga angka
            angka_str = ','.join('{:,}'.format(angka) for angka in angka_list)

            # Mencetak daftar angka dengan pemisah koma
            print("Jumlah angka dalam file:", angka_str)
    except FileNotFoundError:
        print(f"File {file_name} tidak ditemukan.")

def main():
    file_name = "input.txt"  # Nama file yang akan dibaca

    # Memanggil fungsi untuk membaca dan mencetak angka-angka dalam file
    baca_dan_cetak(file_name)

if __name__ == "__main__":
    main()
