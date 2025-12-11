def convert(n, firstVal, secondVal):
    if(firstVal == secondVal): return n
    match firstVal, secondVal:
        case "C","K":
            return n+273.15
        case "C","F":
            return n*1.8+32
        case "F","K":
            return (n-32)*5/9+273.15
        case "F","C":
            return (n-32)*5/9
        case "K","C":
            return n-273.15
        case "K","F":
            return (n-273.15)*1.8+32
        case _:
            print("Nu este o optiune valida")

while True:
    try:
        val=float(input("Introduceti valoarea: \n"))
        firstVal = "a"
        secondVal = "a"
        while not (firstVal =="K" or firstVal =="F" or firstVal == "C"):
            firstVal = input("Introduceti unitatea DIN care sa se faca conversia (K,F,C | KFC): ")
        while not (secondVal =="K" or secondVal =="F" or secondVal == "C"):
            secondVal = input("Introduceti unitatea IN care sa se faca conversia (K,F,C): ")

        if print(f"{val}{firstVal} este {convert(val, firstVal, secondVal):.3f}{secondVal}"):
            break
    except ValueError:
        print("Valorile nu urmeaza cerintele. Reincercati")