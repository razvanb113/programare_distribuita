import math

print ("Introduceti o serie de coordonate pentru a calcula distanta dintre acestea!")

def calculeazaDistanta(x1, y1, x2, y2):
    distanta = math.sqrt(math.pow(x2 - x1, 2) + math.pow(y2 - y1, 2))
    return distanta

punctx1 = 0
puncty1 = 0
punctx2 = 0
puncty2 = 0

while True:
    try:

        punctx1 = int(input("Introduceti coordonata x pentru primul punct: "))
        puncty1 = int(input("Introduceti coordonata y pentru primul punct: "))

        punctx2 = int(input("Introduceti coordonata x pentru al doile punct: "))
        puncty2 = int(input("Introduceti coordonata y pentru al doile punct: "))

        break
    except ValueError:
        print("Ati introdus o data eronata! Incercati din nou!")
        continue

print("Distanta dintre cele 2 puncte este: ", calculeazaDistanta(punctx1, puncty1, punctx2, puncty2))