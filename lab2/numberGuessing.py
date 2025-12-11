import random

numar_secret = random.randint(1, 20)
incercari_ramase = 5

print("Am ales un număr între 1 și 20. Ai 5 încercări să-l ghicești!")

while incercari_ramase > 0:
    try:
        ghicire = int(input("Introdu numărul tău: "))

        if ghicire < 1 or ghicire > 20:
            print("Te rog introdu un număr între 1 și 20.\n")
            continue

        if ghicire < numar_secret:
            print("Prea mic!\n")
        elif ghicire > numar_secret:
            print("Prea mare!\n")
        else:
            print("Corect! Ai ghicit numărul!")
            break

        incercari_ramase -= 1
        print(f"Încercări rămase: {incercari_ramase}\n")

    except ValueError:
        print("Eroare: trebuie să introduci un număr întreg.\n")

if incercari_ramase == 0:
    print(f"Ai pierdut! Numărul era {numar_secret}.")
