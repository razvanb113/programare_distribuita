while True:
    try:
        lista = list(
            map(int, input("Introduceti o serie de numere intregi, separate prin virgula: ").split(","))
        )
        break
    except ValueError:
        print("Valoare introdusa invalida! Reincercati!")


def calculeaza_minim(valori):
    minim = valori[0]
    for x in valori:
        if x < minim:
            minim = x
    return minim


def calculeaza_maxim(valori):
    maxim = valori[0]
    for x in valori:
        if x > maxim:
            maxim = x
    return maxim


print("Minimul din lista citita este:", calculeaza_minim(lista))
print("Maximul din lista citita este:", calculeaza_maxim(lista))
