import tkinter as tk
from tkinter import ttk, messagebox
import requests

class CurrencyConverter:
    def __init__(self, root):
        self.root = root
        self.root.title("Currency Converter")
        self.root.geometry("400x350")
        self.root.resizable(False, False)

        # Culori si stil simplu
        self.bg_color = "#f0f0f0"
        self.root.configure(bg=self.bg_color)

        # Lista de valute uzuale (pentru simplitate)
        self.currencies = ['USD', 'EUR', 'RON', 'GBP', 'CHF', 'JPY', 'CAD', 'AUD']

        self.create_widgets()

    def create_widgets(self):
        # Titlu
        title_label = tk.Label(self.root, text="Convertor Valutar", font=("Arial", 16, "bold"), bg=self.bg_color)
        title_label.pack(pady=20)

        # Frame principal pentru input
        main_frame = tk.Frame(self.root, bg=self.bg_color)
        main_frame.pack(pady=10)

        # Input Suma
        tk.Label(main_frame, text="Suma:", bg=self.bg_color).grid(row=0, column=0, padx=10, pady=10, sticky="w")
        self.amount_entry = tk.Entry(main_frame, width=20)
        self.amount_entry.grid(row=0, column=1, padx=10, pady=10)

        # Selectie Valuta Sursa
        tk.Label(main_frame, text="Din:", bg=self.bg_color).grid(row=1, column=0, padx=10, pady=10, sticky="w")
        self.from_currency = ttk.Combobox(main_frame, values=self.currencies, state="readonly", width=17)
        self.from_currency.current(1) # Default EUR
        self.from_currency.grid(row=1, column=1, padx=10, pady=10)

        # Selectie Valuta Destinatie
        tk.Label(main_frame, text="In:", bg=self.bg_color).grid(row=2, column=0, padx=10, pady=10, sticky="w")
        self.to_currency = ttk.Combobox(main_frame, values=self.currencies, state="readonly", width=17)
        self.to_currency.current(2) # Default RON
        self.to_currency.grid(row=2, column=1, padx=10, pady=10)

        # Buton Convertire
        convert_btn = tk.Button(self.root, text="Converteste", command=self.convert, bg="#4CAF50", fg="white", font=("Arial", 10, "bold"))
        convert_btn.pack(pady=15, ipadx=20)

        # Rezultat
        self.result_label = tk.Label(self.root, text="", font=("Arial", 14), bg=self.bg_color, fg="#333")
        self.result_label.pack(pady=10)

    def convert(self):
        try:
            amount = float(self.amount_entry.get())
            base = self.from_currency.get()
            target = self.to_currency.get()

            if base == target:
                self.result_label.config(text=f"{amount} {target}")
                return

            # Apelare API
            url = f"https://api.frankfurter.app/latest?amount={amount}&from={base}&to={target}"
            response = requests.get(url)
            
            if response.status_code == 200:
                data = response.json()
                converted_amount = data['rates'][target]
                self.result_label.config(text=f"{converted_amount:.2f} {target}")
            else:
                messagebox.showerror("Eroare API", "Nu s-au putut prelua datele.")

        except ValueError:
            messagebox.showwarning("Eroare", "Te rog introdu o suma valida.")
        except requests.exceptions.ConnectionError:
            messagebox.showerror("Eroare Retea", "Verifica conexiunea la internet.")
        except Exception as e:
            messagebox.showerror("Eroare", f"A aparut o problema: {e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = CurrencyConverter(root)
    root.mainloop()