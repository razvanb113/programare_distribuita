print("Acest program va elimina elemntele duplicate dintr-o lista!")

lista1 = []
lista2 = []

while True:
    try:

        lista1 = list(map(int, input("Introduceti o serie de numere intregi, separate prin caracterul ',': ").split(',')))
        break
    except ValueError:
        print("Valoare introdusa invalida! Reincercati!")
        continue

print ("Lista citita este: ", lista1)

for i in lista1:
    if i not in lista2:
        lista2.append(i)

print ("Lista fara elemente duplicate este: ", lista2)