import math_operations


def citire_numere():
    while True:
        try:
            a = float(input("Introduceți primul număr real: "))
            b = float(input("Introduceți al doilea număr real: "))
            return a, b
        except ValueError:
            print("Eroare! Introduceți valori numerice valide.\n")


def main():
    numar1, numar2 = citire_numere()

    print(f"Suma numerelor {numar1} și {numar2} este: {math_operations.adunare(numar1, numar2)}")
    print(f"Diferența numerelor {numar1} și {numar2} este: {math_operations.scadere(numar1, numar2)}")
    print(f"Înmulțirea numerelor {numar1} și {numar2} este: {math_operations.inmultire(numar1, numar2)}")

    try:
        rezultat = math_operations.impartire(numar1, numar2)
        print(f"Împărțirea numerelor {numar1} și {numar2} este: {rezultat}")
    except ZeroDivisionError:
        print("Eroare: împărțire la zero!")


if __name__ == "__main__":
    main()
