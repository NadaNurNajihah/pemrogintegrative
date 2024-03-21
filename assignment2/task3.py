#Nama		    : Nada Nur Najihah
#NIM		    : 239902342
#kelas			: KOM C (PMM)
#Mata Kuliah	: Pemrograman Integrative

class BMI:
    def __init__(self, berat, tinggi_cm):
        self.berat = berat  # dalam kilogram
        self.tinggi = tinggi_cm / 100  # konversi tinggi dari cm ke meter

    def Nilai_BMI(self):
        return self.berat / (self.tinggi ** 2)

# Contoh penggunaan
if __name__ == "__main__":
    berat_seseorang = float(input("Masukkan berat (kg): "))  # dalam kilogram
    tinggi_cm_seseorang = float(input("Masukkan tinggi (cm): "))  # dalam sentimeter

    bmi_calculator = BMI(berat_seseorang, tinggi_cm_seseorang)
    bmi_value = bmi_calculator.Nilai_BMI()

    print("Berat: {} kg".format(berat_seseorang))
    print("Tinggi: {} cm".format(tinggi_cm_seseorang))
    print("Nilai BMI: {:.2f}".format(bmi_value))
