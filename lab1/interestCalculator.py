try:
    principal = int(input("Introduceti principalul: \n"))
    rata = int(input("Introduceti rata anuala (ex: 5): \n"))
    timp = int(input("Introduceti durata, in ani: \n"))

    dobanda = principal * rata * timp / 100
    print(f"Dobanda: {dobanda}")

except ValueError:
    print("Eroare: Introduceti valori intregi!")
