text = input("Introduceti o serie de numere separate prin virgula: ")

lista = []
for element in text.split(","):
    element = element.strip()
    try:
        lista.append(float(element))
    except ValueError:
        print(f"Atentie: '{element}' nu este un numar si a fost ignorat.")

tuplu_numere = tuple(lista)
print("Tupla citita este:", tuplu_numere)

try:
    cautat = float(input("Introduceti elementul pe care doriti sa il cautati: "))

    if cautat in tuplu_numere:
        pozitie = tuplu_numere.index(cautat)
        print(f"Valoarea {cautat} a fost gasita in tuplu la index-ul {pozitie}")
    else:
        print("Elementul nu a fost gasit in tuplu!")
except ValueError:
    print("Valoarea introdusa nu este numar!")
