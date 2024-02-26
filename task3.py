#Nama		    : Nada Nur Najihah
#NIM		    : 239902342
#kelas			: KOM C (PMM)
#Mata Kuliah	: Pemrograman Integrative

print("-------------------------------------")
print("======= PROGRAM =======")
print("-------------------------------------")
angka = int(input('Masukkan Angka : '))

print("Angka yang Anda masukkan kategori : ")

if 0 <= angka < 100:
    print("SMALL")
elif 100 <= angka < 200:
    print("MEDIUM")
elif angka >= 200:
    print("LARGE")
else:
    print("Masukkan Angka Ulang dengan Benar!!!")

