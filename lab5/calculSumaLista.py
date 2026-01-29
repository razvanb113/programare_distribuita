def gaseste_perechi_unice():
    while True:
        try:
            numere = list(map(int, input("Introduceti o serie de numere intregi: ").split()))
            break
        except ValueError:
            print("Valoare introdusa eronata! Reincercati.")

    while True:
        try:
            target = int(input("Introduceti un target: "))
            break
        except ValueError:
            print("Valoare introdusa eronata! Reincercati.\n")

    perechi = set()

    for i in range(len(numere)):
        for j in range(i, len(numere)):
            if numere[i] + numere[j] == target:
                perechi.add((numere[i], numere[j]))

    print("Perechile unice sunt:", perechi)


gaseste_perechi_unice()
