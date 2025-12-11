def convert(n, f, t):
    if f == t: return n
    formulas = {
        ("C","F"): lambda x: x * 1.8 + 32,      ("F","C"): lambda x: (x - 32) / 1.8,
        ("C","K"): lambda x: x + 273.15,        ("K","C"): lambda x: x - 273.15,
        ("F","K"): lambda x: (x - 32)/1.8 + 273.15, ("K","F"): lambda x: (x - 273.15)*1.8 + 32
    }
    return formulas.get((f, t))(n)

while True:
    try:
        val = float(input("Valoarea: "))
        u1 = u2 = ""
        while u1 not in {"C", "F", "K"}: u1 = input("Din (C, F, K): ").upper()
        while u2 not in {"C", "F", "K"}: u2 = input("In (C, F, K): ").upper()
        
        print(f"{val}{u1} este {convert(val, u1, u2):.3f}{u2}")
        break 
    except (ValueError, TypeError):
        print("Date invalide. Reîncercați.")