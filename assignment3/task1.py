#Nama		    : Nada Nur Najihah
#NIM		    : 239902342
#kelas			: KOM C (PMM)
#Mata Kuliah	: Pemrograman Integrative

def main():
    total = 0

    # Membuka file indata.txt untuk membaca
    try:
        with open("indata.txt", "r") as file:
            # Membaca setiap baris dalam file
            for line in file:
                try:
                    # Mengkonversi setiap baris menjadi integer dan menambahkannya ke total
                    number = int(line)
                    total += number
                except ValueError:
                    # Skip baris jika tidak bisa dikonversi menjadi integer
                    continue
    except FileNotFoundError:
        print("File 'indata.txt' tidak ditemukan.")
        return

    # Cetak total dengan format 2 desimal dan menggunakan pemisah ribuan
    print("{:,.2f}".format(total))

if __name__ == "__main__":
    main()
