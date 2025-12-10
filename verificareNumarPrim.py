def prim(n):
    if n<2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n%i==0:
            return False
    return True

numar = int(input("Introduceti un numar: \n"))
if prim(numar):
    print(f"{numar} este un numar prim.")
else: print(f"{numar} nu este un numar prim.")
    