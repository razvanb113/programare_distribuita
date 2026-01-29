print("Acest program elimina elementele duplicate dintr-o lista.")

while True:
    try:
        lista_initiala = list(
            map(int, input("Introduceti numere intregi separate prin virgula: ").split(","))
        )
        break
    except ValueError:
        print("Date invalide! Incercati din nou.")

print("Lista citita este:", lista_initiala)

lista_fara_duplicate = []
for element in lista_initiala:
    if element not in lista_fara_duplicate:
        lista_fara_duplicate.append(element)

print("Lista fara elemente duplicate este:", lista_fara_duplicate)
