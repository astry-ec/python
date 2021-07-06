
def tambah(no1, no2):
    return no1 + no2
def kurang(no1, no2):
    return no1 - no2
def perkalian(no1, no2):
    return no1 * no2
def pembagian(no1, no2):
    return no1 / no2

angka1 = int(input("Masukan Angka 1: "))
angka2 = int(input("Masukan Angka 2: "))
operator = input("Operator (+,-,*,/) : ")
Hasil = 0
  
if operator == '+':
    Hasil += tambah(angka1,angka2)
elif operator == '-':
    Hasil += kurang(angka1,angka2)
elif operator == '*':
    Hasil += perkalian(angka1,angka2)
elif operator == '/':
    Hasil += pembagian(angka1,angka2)
else:
    print("Invalid input")

print(f"Hasil dari {angka1} {operator} {angka2} adalah {Hasil}")