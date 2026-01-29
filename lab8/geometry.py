from geometry import circle, rectangle


def citeste_float(mesaj):
    while True:
        try:
            return float(input(mesaj))
        except ValueError:
            print("Introduceți o valoare numerică validă!\n")


def main():
    raza = citeste_float("Introduceți raza cercului: ")

    print(f"Aria cercului cu raza {raza} este: {circle.Aria(raza)}")
    print(f"Circumferința cercului cu raza {raza} este: {circle.Circumferinta(raza)}")

    print()

    lungime = citeste_float("Introduceți lungimea dreptunghiului: ")
    latime = citeste_float("Introduceți lățimea dreptunghiului: ")

    print(f"Aria dreptunghiului este: {rectangle.Aria(lungime, latime)}")
    print(f"Perimetrul dreptunghiului este: {rectangle.Perimetru(lungime, latime)}")


if __name__ == "__main__":
    main()
