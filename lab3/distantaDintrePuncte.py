import math


def distanta_dintre_puncte(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


print("Introduceti coordonatele a doua puncte pentru a calcula distanta dintre ele.")

while True:
    try:
        x1 = int(input("x1 = "))
        y1 = int(input("y1 = "))
        x2 = int(input("x2 = "))
        y2 = int(input("y2 = "))
        break
    except ValueError:
        print("Date invalide! Introduceti doar numere intregi.\n")


distanta = distanta_dintre_puncte(x1, y1, x2, y2)
print(f"Distanta dintre cele doua puncte este: {distanta}")
