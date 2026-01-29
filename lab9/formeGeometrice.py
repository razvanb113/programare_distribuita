import math

class Shape:
    
    def area(self):
        raise NotImplementedError("Metoda area() trebuie implementată în subclasă!")


class Circle(Shape):
    
    def __init__(self, radius):
      
        if radius <= 0:
            raise ValueError("Raza trebuie să fie pozitivă!")
        self.radius = radius
    
    def area(self):
        return math.pi * self.radius ** 2
    
    def __str__(self):
        return f"Cerc cu raza {self.radius} are aria {self.area():.2f}"


class Rectangle(Shape):
    
    
    def __init__(self, width, height):
        if width <= 0 or height <= 0:
            raise ValueError("Lățimea și înălțimea trebuie să fie pozitive!")
        self.width = width
        self.height = height
    
    def area(self):

        return self.width * self.height
    
    def __str__(self):
        return f"Dreptunghiul cu lungimea de {self.width} si latimea de {self.height} are aria {self.area()}"


if __name__ == "__main__":
    circle = Circle(5)
    rectangle = Rectangle(10, 4)
    
    print(circle)  
    print(rectangle) 
    
    shapes = [
        Circle(3),
        Rectangle(5, 6),
        Circle(7),
        Rectangle(8, 2),
        Circle(4.5)
    ]
    
    print("\nLista de forme geometrice:")
    total_area = 0
    for shape in shapes:
        print(f"{shape}")
        total_area += shape.area()
    
    print(f"\nAria totală a tuturor formelor: {total_area:.2f}")
    
    c1 = Circle(5)
    print(f"Area direct: {c1.area():.2f}")
