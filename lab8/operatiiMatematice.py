import math

numar = 0
unghi = 0

while True:
    try:
        numar = int(input("Introduceti un numar intreg: "))
        unghi = int(input("Introduceti o valoare pentru unghi, in grade: "))
        break
    except (ValueError):
        print("Introduceti valori corecte!")
        continue

print(f"Rădăcina pătrată a {numar} este {math.sqrt(numar)}")
print(f"Factorialul lui {numar} este {math.factorial(numar)}")
print(f"Sinusul unghiului de {unghi} grade este {math.sin(math.radians(unghi))}")