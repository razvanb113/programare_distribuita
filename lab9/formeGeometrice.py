import math


class Shape:
    def area(self):
        raise NotImplementedError("Metoda area() trebuie implementata in subclasa!")


class Circle(Shape):
    def __init__(self, raza):
        if raza <= 0:
            raise ValueError("Raza trebuie sa fie pozitiva!")
        self.raza = raza

    def area(self):
        return math.pi * self.raza ** 2

    def __str__(self):
        return f"Cerc cu raza {self.raza} are aria {self.area():.2f}"


class Rectangle(Shape):
    def __init__(self, latime, inaltime):
        if latime <= 0 or inaltime <= 0:
            raise ValueError("Latimea si inaltimea trebuie sa fie pozitive!")
        self.latime = latime
        self.inaltime = inaltime

    def area(self):
        return self.latime * self.inaltime

    def __str__(self):
        return (
            f"Dreptunghi cu latimea {self.latime} si inaltimea {self.inaltime} "
            f"are aria {self.area()}"
        )


if __name__ == "__main__":
    cerc = Circle(5)
    dreptunghi = Rectangle(10, 4)

    print(cerc)
    print(dreptunghi)

    forme = [
        Circle(3),
        Rectangle(5, 6),
        Circle(7),
        Rectangle(8, 2),
        Circle(4.5)
    ]

    print("\nLista de forme geometrice:")
    aria_totala = 0

    for forma in forme:
        print(forma)
        aria_totala += forma.area()

    print(f"\nAria totala a tuturor formelor: {aria_totala:.2f}")

    c1 = Circle(5)
    print(f"Aria calculata direct: {c1.area():.2f}")
