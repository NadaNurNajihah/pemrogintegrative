#Nama		    : Nada Nur Najihah
#NIM		    : 239902342
#kelas			: KOM C (PMM)
#Mata Kuliah	: Pemrograman Integrative

class BMI:
    def __init__(self, berat, tinggi_cm):
        self.berat = berat  # dalam kilogram
        self.tinggi = tinggi_cm / 100  # konversi tinggi dari cm ke meter

    def BMI_Value(self):
        return self.berat / (self.tinggi ** 2)

    def __eq__(self, other):
        if isinstance(other, BMI):
            return self.berat == other.berat and self.tinggi == other.tinggi
        return False

# Contoh penggunaan
if __name__ == "__main__":
    try:
        berat = float(input("Masukkan berat (kg): "))
        tinggi_cm = float(input("Masukkan tinggi (cm): "))
    except ValueError:
        print("Masukkan angka yang valid untuk berat dan tinggi.")
    else:
        bmi1 = BMI(berat, tinggi_cm)

        print("BMI Value:", bmi1.BMI_Value())

        try:
            berat2 = float(input("Masukkan berat untuk BMI kedua (kg): "))
            tinggi_cm2 = float(input("Masukkan tinggi untuk BMI kedua (cm): "))
        except ValueError:
            print("Masukkan angka yang valid untuk berat dan tinggi kedua.")
        else:
            bmi2 = BMI(berat2, tinggi_cm2)

            print("BMI Value (BMI kedua):", bmi2.BMI_Value())

            if bmi1 == bmi2:
                print("BMI 1 dan BMI 2 memiliki berat dan tinggi yang sama.")
            else:
                print("BMI 1 dan BMI 2 memiliki berat dan/atau tinggi yang berbeda.")
