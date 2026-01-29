from geometry import circle
from geometry import rectangle

while True:
    try:
        raza = float(input("Introduceti raza cercului: "))
        break
    except ValueError:
        print("Introduceti o valoare numerica valida!")
        continue

print(f"Aria cercului cu raza {raza} este: {circle.Aria(raza)}")
print(f"Circumferinta cercului cu raza {raza} este: {circle.Circumferinta(raza)}")

print()

while True:
    try:
        lungime = float(input("Introduceti lungimea dreptunghiului: "))
        latime = float(input("Introduceti latimea dreptunghiului: "))
        break
    except ValueError:
        print("Introduceti valori numerice valide!")
        continue

print(f"Aria dreptunghiului este: {rectangle.Aria(lungime, latime)}")
print(f"Perimetrul dreptunghiului este: {rectangle.Perimetru(lungime, latime)}")
