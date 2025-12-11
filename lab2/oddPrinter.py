while True:
    try:
        n = int(input("Introdu un număr n: "))
        break
    except ValueError:
        print("Eroare: te rog introdu un număr întreg valid.\n")

print(f"Numerele impare până la {n} sunt:")

for i in range(1, n + 1, 2):
    print(i, end=", " if i + 2 <= n else "")
