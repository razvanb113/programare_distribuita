numere = input("Introduceti o serie de numere separate prin virgula: ")
elemente = numere.split(',')

lista_numere = []

for i in elemente:
    i = i.strip()

    try:
        numar = float(i)
        lista_numere.append(numar)
    except ValueError:
        print(f"Atentie: {i} nu este numar si a fost ignorat.")

tupla = tuple(lista_numere)

print ("Tupla citita este: ", tupla)

try:
    element_cautare = float(input("Introduceti elementul pe care doriti sa il cautati: "))

    if element_cautare in tupla:
        index = tupla.index(element_cautare)
        print(f"Valoarea {element_cautare} a fost gasit in tuplu la index-ul {index}")
    else:
        print("Elementul nu a fost gasit in tuplu!")

except ValueError:
    print("Valoarea introdusa nu este numar!")