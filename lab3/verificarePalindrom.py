print("Acest program verifica daca un cuvant este palindrom.")

def verifica_palindrom(cuvant):
    invers = cuvant[::-1]

    print(invers)

    if cuvant == invers:
        print("Cuvantul introdus este palindrom!")
    else:
        print("Cuvantul introdus nu este palindrom!")


while True:
    text = input("Introduceti un cuvant: ").strip()

    if not text:
        print("Nu a fost introdus niciun cuvant!")
    elif text.isdigit():
        print("Introduceti doar cuvinte!")
    else:
        break


verifica_palindrom(text)
