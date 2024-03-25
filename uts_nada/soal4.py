#Nama		    : Nada Nur Najihah
#NIM		    : 239902342
#kelas			: KOM C (PMM)
#Mata Kuliah	: Pemrograman Integrative
####### UTS #########

class BMI:
    def __init__(self, berat, tinggi):
        self.berat = berat  # dalam satuan pound
        self.tinggi = tinggi  # dalam satuan kaki

    @property
    def bmi_value(self):
        tinggi_meter = self.tinggi * 0.3048  # konversi tinggi dari kaki ke meter
        berat_kg = self.berat * 0.453592  # konversi berat dari pound ke kg
        bmi = berat_kg / (tinggi_meter ** 2)  # hitung BMI
        return bmi

    def __eq__(self, other):
        if isinstance(other, BMI):
            # Bandingkan berat dan tinggi dari dua objek BMI
            return self.berat == other.berat and self.tinggi == other.tinggi
        return False

# Contoh penggunaan
bmi1 = BMI(150, 5.5)  # berat: 150 pound, tinggi: 5.5 kaki
bmi2 = BMI(180, 6.0)  # berat: 180 pound, tinggi: 6.0 kaki

# Cetak nilai BMI
print("BMI 1:", bmi1.bmi_value)
print("BMI 2:", bmi2.bmi_value)

# Bandingkan dua objek BMI
if bmi1 == bmi2:
    print("BMI 1 dan BMI 2 memiliki berat dan tinggi yang sama.")
else:
    print("BMI 1 dan BMI 2 memiliki berat dan/atau tinggi yang berbeda.")
