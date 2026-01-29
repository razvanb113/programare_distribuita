print("Introduceti un numar caruia sa i se calculeze factorialul!")

numar = 0

def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

while True:
    try:
        numar = int(input("Introduceti un numar: "))

        if numar < 0:
            print("Numarul introdus trebuie sa fie mai mare decat 0!")
            continue

        break
    except ValueError:
        print("Nu ati introdus un numar! Incercati din nou!")
        continue

print("Factorialul numarului", numar, "este: ", factorial(numar))