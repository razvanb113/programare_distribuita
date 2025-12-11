try:
    celsius = float(input("Introduceti gradele Celsius: "))
    fahrenheit = celsius * 1.8 + 32
    print(f"{celsius}C = {fahrenheit}F")
except ValueError:
    print("Eroare: Introduceti un numar valid pentru gradele Celsius!")
