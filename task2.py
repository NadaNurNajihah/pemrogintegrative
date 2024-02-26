#Nama		    : Nada Nur Najihah
#NIM		    : 239902342
#kelas			: KOM C (PMM)
#Mata Kuliah	: Pemrograman Integrative


print("-------------------------------------")
print("======= PROGRAM PEMBAGIAN 3 =======")
print("-------------------------------------")
angka = int(input('Masukkan Angka : '))

jml = angka/3

# Memakai round() untuk membulatkan ke 3 angka desimal
jml_bulat = round(jml, 3)

print("Hasil Pembagiannya adalah : {:.3f}".format(jml_bulat))
