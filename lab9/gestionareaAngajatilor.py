class Employee:
    
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    
    def get_details(self):
        return f"Employee: {self.name}, Salary: {self.salary}"


class Manager(Employee):
    
    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.department = department
    
    def get_details(self):
        return f"Manager: {self.name}, Salary: {self.salary}, Department: {self.department}"


if __name__ == "__main__":
    emp = Employee("John", 3000)
    print(emp.get_details()) 
    
    mgr = Manager("Alice", 5000, "IT")
    print(mgr.get_details())
    
    print("\n" + "="*50)
    print("Demonstrație moștenire și polimorfism:")
    print("="*50)
    
   
    employees = [
        Employee("John", 3000),
        Employee("Maria", 3500),
        Manager("Alice", 5000, "IT"),
        Manager("Bob", 5500, "HR"),
        Employee("Dan", 2800)
    ]
    
    print("\nLista de angajați:")
    for emp in employees:
        print(f" {emp.get_details()}")
    
    print("\n" + "="*50)
    print("Verificare tipuri (isinstance):")
    print("="*50)
    for emp in employees:
        if isinstance(emp, Manager):
            print(f"✓ {emp.name} este Manager")
        elif isinstance(emp, Employee):
            print(f"  {emp.name} este Employee")
