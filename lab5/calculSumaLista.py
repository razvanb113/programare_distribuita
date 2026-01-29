numere = []
perechi = set()

def unique_pair(numere, perechi):

    while True:
        try:
            numere = list(map(int, input("Introduceti o serie de numere intregi: ").split()))
            break
        except (ValueError):
            print("Valoare introdusa eronata!Reincercati")
            continue

    while True:
        try:
            target = int(input("Introduceti un target: "))
            break
        except (ValueError):
            print("Valoare introdusa eronat!Reincercati!\n")
            continue

    for i in range(len(numere)):
        for j in range(i, len(numere)):
            if numere[i] + numere[j] == target:
                perechi.add((numere[i], numere[j]))

    print(perechi)

unique_pair(numere, perechi)