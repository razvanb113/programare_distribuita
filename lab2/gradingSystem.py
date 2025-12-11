while True:
    try:
        scor = int(input("Introduceti un scor procentual: "))
        if 0 <= scor <= 100:
            break
    except ValueError:
        print("Introduceti o valoare intreaga intre 0 si 100.")

scor/=10
match int(scor):
    case 10|9:
        print("Nota A\n")
    case 8:
        print("Nota B\n")
    case 7:
        print("Nota C\n")
    case 6:
        print("Nota D\n")
    case _:
        print("Nota F\n")