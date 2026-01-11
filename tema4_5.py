def gestioneaza_magazin():
    preturi_produse = {
        "mere": 1.0, 
        "banane": 0.5, 
        "portocale": 0.8, 
        "mango": 1.5
    }

    stoc_curent = {
        "mere": 10, 
        "banane": 20, 
        "portocale": 15, 
        "mango": 5
    }

    vanzari_zi = [
        ("mere", 4), 
        ("banane", 6), 
        ("portocale", 10), 
        ("mango", 2)
    ]

    venit_total = 0.0

    for produs, cantitate_vanduta in vanzari_zi:
        if produs in stoc_curent and produs in preturi_produse:
            valoare_vanzare = preturi_produse[produs] * cantitate_vanduta
            venit_total += valoare_vanzare
            
            stoc_curent[produs] -= cantitate_vanduta
        else:
            print(f"Atenție: Produsul '{produs}' nu a fost găsit în inventar.")

    produse_de_realimentat = set()
    
    for produs, cantitate in stoc_curent.items():
        if cantitate < 5:
            produse_de_realimentat.add(produs)

    print("--- Raport Zilnic Magazin ---")
    print(f"Venit total: {venit_total} RON")
    
    print("\nStocuri rămase:")
    for produs, cantitate in stoc_curent.items():
        print(f"  - {produs}: {cantitate}")
        
    print("\nProduse ce necesită realimentare:")
    if produse_de_realimentat:
        for produs in produse_de_realimentat:
            print(f"  - {produs}")
    else:
        print("  - Niciun produs nu necesită realimentare.")

if __name__ == "__main__":
    gestioneaza_magazin()