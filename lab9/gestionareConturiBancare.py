class ContBancar:
    def __init__(self, sold_initial=0):
        if sold_initial < 0:
            raise ValueError("Soldul inițial nu poate fi negativ!")
        self.__sold = sold_initial

    def depune(self, suma):
        if suma <= 0:
            raise ValueError("Suma depusă trebuie să fie pozitivă!")
        self.__sold += suma
        print(f"Depunere: {suma} RON | Sold actual: {self.__sold} RON")
        return self.__sold

    def retrage(self, suma):
        if suma <= 0:
            raise ValueError("Suma retrasă trebuie să fie pozitivă!")
        if suma > self.__sold:
            raise ValueError(
                f"Fonduri insuficiente! Disponibil: {self.__sold} RON, Cerut: {suma} RON"
            )
        self.__sold -= suma
        print(f"Retragere: {suma} RON | Sold actual: {self.__sold} RON")
        return self.__sold

    def sold_curent(self):
        return self.__sold


def afiseaza_meniu():
    print("\n" + "-" * 40)
    print("      MENIU CONT BANCAR")
    print("-" * 40)
    print("1. Afișare sold")
    print("2. Depunere")
    print("3. Retragere")
    print("4. Ieșire")
    print("-" * 40)


def citeste_float(mesaj):
    try:
        return float(input(mesaj))
    except ValueError:
        raise ValueError("Introduceți o valoare numerică validă!")


def ruleaza_aplicatia():
    while True:
        try:
            sold = citeste_float("\nIntroduceți soldul inițial (RON): ")
            cont = ContBancar(sold)
            print(f"Cont creat! Sold inițial: {cont.sold_curent()} RON")
            break
        except ValueError as err:
            print(f"Eroare: {err}")

    while True:
        afiseaza_meniu()

        try:
            optiune = input("Selectați o opțiune (1-4): ").strip()

            if optiune == "1":
                print(f"\nSold curent: {cont.sold_curent()} RON")

            elif optiune == "2":
                suma = citeste_float("Suma de depus (RON): ")
                cont.depune(suma)
                print("Operațiune finalizată cu succes!")

            elif optiune == "3":
                suma = citeste_float("Suma de retras (RON): ")
                cont.retrage(suma)
                print("Operațiune finalizată cu succes!")

            elif optiune == "4":
                print(f"\nSold final: {cont.sold_curent()} RON")
                break

            else:
                print("Opțiune invalidă! Alegeți între 1 și 4.")

        except KeyboardInterrupt:
            print("\n\nAplicația a fost oprită de utilizator.")
            print(f"Sold final: {cont.sold_curent()} RON")
            break
        except ValueError as err:
            print(f"Eroare: {err}")
        except Exception as err:
            print(f"Eroare neașteptată: {err}")


if __name__ == "__main__":
    ruleaza_aplicatia()
