#Nama		    : Nada Nur Najihah
#NIM		    : 239902342
#kelas			: KOM C (PMM)
#Mata Kuliah	: Pemrograman Integrative


print("------------------------------------------")
print("Program Penjumlahan Bilangan Berturut-turut")
print("------------------------------------------")

angka = int(input("Masukkan sebuah angka: "))

# Menggunakan rumus penjumlahan deret aritmatika ((n(n+1))/2)
jumlah = (angka * (angka + 1)) // 2

print("Jumlah dari 1 hingga", angka, "adalah:", jumlah)
