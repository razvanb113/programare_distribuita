def convert(n, firstVal, secondVal):
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
        case "K",