class BankAccount:
    def __init__(self, initial_balance=0):
        if initial_balance < 0:
            raise ValueError("Soldul inițial nu poate fi negativ!")
        self._balance = initial_balance
    
    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Suma depusă trebuie să fie pozitivă!")
        self._balance += amount
        print(f"Depunere: {amount} RON. Sold nou: {self._balance} RON")
        return self._balance
    
    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Suma retrasă trebuie să fie pozitivă!")
        if amount > self._balance:
            raise ValueError(f"Sold insuficient! Disponibil: {self._balance} RON, Solicitat: {amount} RON")
        self._balance -= amount
        print(f"Retragere: {amount} RON. Sold nou: {self._balance} RON")
        return self._balance
    
    def get_balance(self):
        return self._balance


def show_menu():
    """Afișează meniul principal."""
    print("\n" + "="*40)
    print("   MENIU GESTIONARE CONT BANCAR")
    print("="*40)
    print("1. Verifică sold")
    print("2. Depune bani")
    print("3. Retrage bani")
    print("4. Ieșire")
    print("="*40)


def main():
    
    while True:
        try:
            initial_balance = float(input("\nIntroduceți soldul inițial al contului (RON): "))
            cont = BankAccount(initial_balance)
            print(f"\nCont creat cu succes! Sold inițial: {cont.get_balance()} RON")
            break
        except ValueError as e:
            print(f"Eroare: {e}")
        except Exception as e:
            print(f"Eroare: Introduceți un număr valid!")
    
    while True:
        show_menu()
        
        try:
            choice = input("\nAlegeți o opțiune (1-4): ").strip()
            
            if choice == "1":
                print(f"\n Soldul curent: {cont.get_balance()} RON")
            
            elif choice == "2":
                try:
                    amount = float(input("Introduceți suma de depus (RON): "))
                    cont.deposit(amount)
                    print(f"Operațiune reușită!")
                except ValueError as e:
                    print(f"Eroare: {e}")
                except Exception as e:
                    print(f"Eroare: Introduceți un număr valid!")
            
            elif choice == "3":
                try:
                    amount = float(input("Introduceți suma de retras (RON): "))
                    cont.withdraw(amount)
                    print(f"Operațiune reușită!")
                except ValueError as e:
                    print(f"Eroare: {e}")
                except Exception as e:
                    print(f"Eroare: Introduceți un număr valid!")
            
            elif choice == "4":
                print(f"\n Sold final: {cont.get_balance()} RON")
                break
            
            else:
                print("Opțiune invalidă! Alegeți un număr între 1 și 4.")
        
        except KeyboardInterrupt:
            print("\n\nProgram întrerupt de utilizator.")
            print(f"Sold final: {cont.get_balance()} RON")
            break
        except Exception as e:
            print(f"Eroare neașteptată: {e}")


if __name__ == "__main__":
    main()
