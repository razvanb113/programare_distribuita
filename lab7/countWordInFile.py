def numara_cuvinte_fisier(nume_fisier):
    try:
        fisier = open(nume_fisier, "r")
        text = fisier.read()
        fisier.close()
    except FileNotFoundError:
        print("Fișierul nu a fost găsit!")
        return 0

    cuvinte = text.split()
    nr_cuvinte = 0

    for cuvant in cuvinte:
        nr_cuvinte += 1

    return nr_cuvinte


rezultat = numara_cuvinte_fisier("countWordInFile.txt")
print("Numărul de cuvinte din fișier este:", rezultat)
