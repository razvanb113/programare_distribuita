def calculeaza_factorial(x):
    rezultat = 1
    for i in range(1, x + 1):
        rezultat *= i
    return rezultat


print("Introduceti un numar pentru calcularea factorialului!")

while True:
    try:
        numar = int(input("Numar: "))
        if numar < 0:
            print("Numarul trebuie sa fie pozitiv!")
        else:
            break
    except ValueError:
        print("Valoare invalida! Va rugam introduceti un numar intreg.")


print(f"Factorialul numarului {numar} este: {calculeaza_factorial(numar)}")
def calculeaza_factorial(x):
    rezultat = 1
    for i in range(1, x + 1):
        rezultat *= i
    return rezultat


print("Introduceti un numar pentru calcularea factorialului!")

while True:
    try:
        numar = int(input("Numar: "))
        if numar < 0:
            print("Numarul trebuie sa fie pozitiv!")
        else:
            break
    except ValueError:
        print("Valoare invalida! Va rugam introduceti un numar intreg.")


print(f"Factorialul numarului {numar} este: {calculeaza_factorial(numar)}")
