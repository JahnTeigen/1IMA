import math
import time

v="Versjon - 3.1" 

print("")
print("=======================================================================")
print("                           BMI Kalkulator")
print("                        Presentert av Matvey")
print("                          ", v)
print("=======================================================================")
print("")

def utregning(vekt, høyde, alder, system):

    try:
        if vekt <= 0 or høyde <= 0:
            raise ValueError("Vekt og Høyde må være positive verdier")
        
        if system == 'M' or system =='m':
            bmi = (vekt / (høyde * høyde)) * 10000
        else:
            bmi = 703 * (vekt / (høyde * høyde))

        if bmi < 18.5:
            kategori = "Undervektig"
        elif 18.5 <= bmi < 24.9:
            kategori = "Normal vekt"
        elif 25 <= bmi < 29.9:
            kategori = "Overvektig"
        else:
            kategori = "Overvektig ++"

        if not(12<= alder <=25):
            warning = "OBS! Resultatet kan være unøyaktig for aldre utenfor 12-25."
        else:
            warning = ""

        return round(bmi, 2), kategori, warning

    except Exception as e:
        return str(e), "", ""

system = input("Velg målenhet (M for metrisk I for imperial): ")
if system in("M", "m"):
    vekt = float(input("Vekt i kg: "))
    høyde = float(input("Høyde i cm: "))
else:
    vekt = float(input("Vekt i lbs: "))
    høyde = float(input("Høyde i inches: "))
alder = int(input("Alder: "))
result, kategori, warning = utregning(vekt, høyde, alder, system)

for i in range(3):
    time.sleep(0.5)
    print("Working.")
    time.sleep(0.5)
    print("Working..")
    time.sleep(0.5)
    print("Working...")

time.sleep(1)

print("")
print('BMI: ', result)
print('Kategori: ', kategori)
print(warning)
print("")
print("-----------------------------------")
print("| Bmi resultatet forklart:        |")
print("| BMI < 18.5 = Undervektig        |")
print("| BMI   18.5 - 24.9 = Normal Vekt |")
print("| BMI   24.9 - 29.9 = Overvektig  |")
print("| BMI > 29.9 = Overvektig ++      |")
print("-----------------------------------")
print("")
print(v," Produsert av Matvey.   © 2006-2024 Matvey Golovtsov")
