#Nama		    : Nada Nur Najihah
#NIM		    : 239902342
#kelas			: KOM C (PMM)
#Mata Kuliah	: Pemrograman Integrative

from datetime import datetime, timedelta
import locale

# Atur locale untuk Bahasa Indonesia
locale.setlocale(locale.LC_TIME, 'id_ID.UTF-8')

def print_future_date(num_days):
    # Dapatkan tanggal saat ini
    current_date = datetime.now()

    # Hitung tanggal di masa depan
    future_date = current_date + timedelta(days=num_days)

    # Format tanggal di masa depan
    formatted_date = future_date.strftime("%A, %d %B %Y")
    
    print("Tanggal {} hari dari sekarang akan menjadi: {}".format(num_days, formatted_date))

if __name__ == "__main__":
    try:
        days = int(input("Masukkan jumlah hari dari sekarang: "))
        print_future_date(days)
    except ValueError:
        print("Silakan masukkan jumlah hari yang valid.")
