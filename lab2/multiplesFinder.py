def citeste_numere():
    while True:
        try:
            x = int(input("Introdu numărul x: "))
            y = int(input("Introdu numărul y: "))

            if x == 0:
                print("x nu poate fi 0. Reîncearcă.\n")
                continue

            return x, y

        except ValueError:
            print("Eroare: trebuie să introduci numere întregi valide. Reîncearcă.\n")

x, y = citeste_numere()

print(f"\nMultiplii lui {x} mai mici decât {y} sunt:")
exista = False

for i in range(x, y, x):
    print(i)
    exista = True

if not exista:
    print("Nu există astfel de multipli.")