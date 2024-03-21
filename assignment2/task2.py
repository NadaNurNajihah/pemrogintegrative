#Nama		    : Nada Nur Najihah
#NIM		    : 239902342
#kelas			: KOM C (PMM)
#Mata Kuliah	: Pemrograman Integrative

print("------------------------------------------")
print("Program Penjumlahan Angka (Masukkan -1 untuk berhenti)")
print("------------------------------------------")

total = 0
while True:
    angka = int(input(" Masukkan Angka : "))
    if angka == -1:
        break
    total += angka

print("Jumlah dari semua angka yang dimasukkan adalah: {:.2f}".format(total))
