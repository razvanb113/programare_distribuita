print ("Acest program va returna true daca un cuvant citit de la tastatura este palindrom, fals altfel")

def is_palindrome(text):
    cleaned_text = text.replace(" ", "").lower()
    
    invers = ""

    for i in range(len(cleaned_text) - 1, -1, -1):
        invers += cleaned_text[i]

    print(invers)

    if invers == cleaned_text:
        print("Cuvantul introdus este palindrom!")
    else:
        print("Cuvantul introdus nu este palindrom!")


while True:
    text = input("Introduceti un cuvant: ")

    if text.strip() == "":
        print("Nu a fost introdus nimic!")
        continue
    elif text.isdigit():
        print("Introduceti doar cuvinte!")
        continue

    break

is_palindrome(text)

