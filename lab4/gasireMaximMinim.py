l1 = []

while True:

    try:

        l1 = list(map(int, input("Introduceti o serie de numere intregi, separate prin caracterul ',': ").split(',')))
        break
    except ValueError:
        print("Valoare introdusa invalida! Reincercati!")
        continue

def min(l1):
    minimul = l1[0]
    for x in l1:
        if x < minimul:
            minimul = x
    return minimul

def max(l1):
    maximul = l1[0]
    for x in l1:
        if x > maximul:
            maximul = x
    return maximul

print("Minimul din lista citita este: ", min(l1))
print("Maximul din lista citita este: ", max(l1))