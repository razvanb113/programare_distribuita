text = input("Introduceti o propozitie: ").split()

#text.lower()

frecventa_cuvinte = {}

for cuvant1 in text:
    contor = 0
    for cuvant2 in text:
        if cuvant1 == cuvant2:
            contor += 1
        else:
            continue
    frecventa_cuvinte[cuvant1] = contor

print(frecventa_cuvinte)