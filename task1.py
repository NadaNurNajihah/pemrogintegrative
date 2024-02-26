
#Nama		    : Nada Nur Najihah
#NIM		    : 239902342
#kelas			: KOM C (PMM)
#Mata Kuliah	: Pemrograman Integrative


print("-------------------------------------")
print("======= PROGRAM GAJI KARYAWAN =======")
print("-------------------------------------")
nama = input("NAMA KARYAWAN : ")
tgl = input("Tanggal sekarang (dd/mm/yyyy) : ")
gaji = int(input("Masukkan Gaji Anda : "))

gajipokok = gaji / 12

print("--------------------------------------")
print("=========== GAJI KARYAWAN ============")
print("--------------------------------------")
print("Nama : ", nama)
print("Tanggal/bulan/tahun : ", tgl)
print("Gaji Pokok Anda : Rp.", gajipokok)
