import math_operations

numar1 = 0
numar2 = 0

while True:

    try:
        numar1 = float(input("Introduceti primul numar real: "))
        numar2 = float(input("Introduceti al doilea numar real: "))
        break

    except(ValueError):
        print("Introduceti valori corecte!")
        continue

print("Suma numerelor", numar1 , "cu", numar2, "este: ", math_operations.adunare(numar1, numar2))
print("Diferenta numerelor", numar1 , "cu", numar2, "este: ", math_operations.scadere(numar1, numar2))
print("Inmultirea numerelor", numar1 , "cu", numar2, "este: ", math_operations.inmultire(numar1, numar2))
print("Impartirea numerelor", numar1 , "cu", numar2, "este: ", math_operations.impartire(numar1, numar2) )

    