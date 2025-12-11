try:
    n = int(input("Introduceti un numar intreg: \n"))
    
    if n % 2:
        print("Numarul este impar")
    else:
        print("Numarul este par")

except ValueError:
    print("Eroare: Introduceti un numar intreg valid!")
