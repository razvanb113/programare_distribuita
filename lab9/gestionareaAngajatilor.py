class Employee:
    def __init__(self, nume, salariu):
        self.nume = nume
        self.salariu = salariu

    def get_details(self):
        return f"Employee: {self.nume}, Salary: {self.salariu}"


class Manager(Employee):
    def __init__(self, nume, salariu, departament):
        super().__init__(nume, salariu)
        self.departament = departament

    def get_details(self):
        return (
            f"Manager: {self.nume}, Salary: {self.salariu}, "
            f"Department: {self.departament}"
        )


if __name__ == "__main__":
    angajat = Employee("John", 3000)
    print(angajat.get_details())

    manager = Manager("Alice", 5000, "IT")
    print(manager.get_details())

    print("\n" + "=" * 50)
    print("Demonstratie mostenire si polimorfism:")
    print("=" * 50)

    lista_angajati = [
        Employee("John", 3000),
        Employee("Maria", 3500),
        Manager("Alice", 5000, "IT"),
        Manager("Bob", 5500, "HR"),
        Employee("Dan", 2800)
    ]

    print("\nLista de angajati:")
    for persoana in lista_angajati:
        print(f" {persoana.get_details()}")

    print("\n" + "=" * 50)
    print("Verificare tipuri (isinstance):")
    print("=" * 50)

    for persoana in lista_angajati:
        if isinstance(persoana, Manager):
            print(f"✓ {persoana.nume} este Manager")
        else:
            print(f"  {persoana.nume} este Employee")
