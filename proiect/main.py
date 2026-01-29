import tkinter as tk
from tkinter import ttk, messagebox
import requests
import threading # Folosit pentru a nu bloca fereastra cand se incarca datele

class CurrencyConverter:
    def __init__(self, root):
        self.root = root
        self.root.title("Convertor Valutar & Cursuri")
        # Am marit fereastra pentru a incapea ambele sectiuni
        self.root.geometry("650x400") 
        self.root.resizable(False, False)

        # Culori si stil
        self.bg_color = "#f4f4f9"
        self.root.configure(bg=self.bg_color)
        
        # Lista de valute
        self.currencies = ['USD', 'EUR', 'RON', 'GBP', 'CHF', 'JPY', 'CAD', 'AUD']

        # Configurare Layout (Stanga si Dreapta)
        self.setup_layout()

        # Pornim incarcarea cursurilor principale automat
        self.load_major_rates()

    def setup_layout(self):
        # === FRAME STANGA: CONVERTOR ===
        left_frame = tk.Frame(self.root, bg=self.bg_color) # Am scos width de aici, lasam sa se extinda
        left_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=20, pady=20)

        # Titlu Convertor
        tk.Label(left_frame, text="Convertor", font=("Segoe UI", 16, "bold"), bg=self.bg_color, fg="#333").pack(pady=(0, 20))

        # Input Suma
        input_frame = tk.Frame(left_frame, bg=self.bg_color)
        input_frame.pack(fill=tk.X, pady=5)
        tk.Label(input_frame, text="Suma:", bg=self.bg_color).pack(anchor="w")
        self.amount_entry = tk.Entry(input_frame, font=("Segoe UI", 11))
        self.amount_entry.pack(fill=tk.X, pady=2)

        # Selectie Valute
        grid_frame = tk.Frame(left_frame, bg=self.bg_color)
        grid_frame.pack(fill=tk.X, pady=10)

        # Din
        tk.Label(grid_frame, text="Din:", bg=self.bg_color).grid(row=0, column=0, sticky="w", padx=5)
        self.from_currency = ttk.Combobox(grid_frame, values=self.currencies, state="readonly", width=12)
        self.from_currency.current(1) # Default EUR
        self.from_currency.grid(row=1, column=0, padx=5)

        # In
        tk.Label(grid_frame, text="În:", bg=self.bg_color).grid(row=0, column=1, sticky="w", padx=5)
        self.to_currency = ttk.Combobox(grid_frame, values=self.currencies, state="readonly", width=12)
        self.to_currency.current(2) # Default RON
        self.to_currency.grid(row=1, column=1, padx=5)

        # Buton Convertire
        convert_btn = tk.Button(left_frame, text="Calculează", command=self.convert, bg="#4CAF50", fg="white", font=("Segoe UI", 11, "bold"), bd=0, padx=10, pady=5)
        convert_btn.pack(pady=20, fill=tk.X)

        # Rezultat
        self.result_label = tk.Label(left_frame, text="---", font=("Segoe UI", 16, "bold"), bg=self.bg_color, fg="#2c3e50")
        self.result_label.pack(pady=10)

        # === SEPARATOR VERTICAL ===
        ttk.Separator(self.root, orient='vertical').pack(side=tk.LEFT, fill='y', pady=20)

        # === FRAME DREAPTA: CURSURI PRINCIPALE ===
        # CORECTIA ESTE AICI: width=250 este pus in tk.Frame, nu in pack
        right_frame = tk.Frame(self.root, bg="#e8e8e8", width=250) 
        right_frame.pack(side=tk.RIGHT, fill=tk.BOTH, padx=0) 
        
        # Container intern cu padding
        self.rates_container = tk.Frame(right_frame, bg="#e8e8e8")
        self.rates_container.pack(padx=20, pady=20, fill=tk.BOTH)

        tk.Label(self.rates_container, text="Principalele Cursuri\n(vs RON)", font=("Segoe UI", 14, "bold"), bg="#e8e8e8", fg="#555").pack(pady=(0, 15))

        # Placeholder pentru lista de cursuri
        self.rates_labels = {}
        major_currencies = ['EUR', 'USD', 'GBP', 'CHF']
        
        for currency in major_currencies:
            row = tk.Frame(self.rates_container, bg="white", pady=5, padx=5)
            row.pack(fill=tk.X, pady=5)
            
            lbl_name = tk.Label(row, text=f"1 {currency}", font=("Segoe UI", 10, "bold"), bg="white", width=6, anchor="w")
            lbl_name.pack(side=tk.LEFT)
            
            lbl_val = tk.Label(row, text="...", font=("Segoe UI", 10), bg="white", fg="#4CAF50")
            lbl_val.pack(side=tk.RIGHT)
            
            self.rates_labels[currency] = lbl_val

        # Buton refresh mic
        refresh_btn = tk.Button(self.rates_container, text="Actualizează Cursuri", command=self.load_major_rates, font=("Segoe UI", 8), bg="#ddd")
        refresh_btn.pack(pady=20)

    def load_major_rates(self):
        """ Ruleaza request-ul API intr-un thread separat sa nu blocheze interfata """
        thread = threading.Thread(target=self.fetch_rates_thread)
        thread.start()

    def fetch_rates_thread(self):
        major_currencies = ['EUR', 'USD', 'GBP', 'CHF']
        
        try:
            # Facem un loop pentru a lua cursurile fiecaruia fata de RON
            for curr in major_currencies:
                # URL Corectat
                url = f"https://api.frankfurter.app/latest?amount=1&from={curr}&to=RON"
                response = requests.get(url)
                
                if response.status_code == 200:
                    data = response.json()
                    valoare = data['rates']['RON']
                    
                    # Actualizam interfata grafica din thread
                    self.root.after(0, self.update_rate_label, curr, valoare)
        except Exception as e:
            print(f"Eroare la preluarea cursurilor: {e}")

    def update_rate_label(self, currency, value):
        if currency in self.rates_labels:
            self.rates_labels[currency].config(text=f"{value:.4f} RON")

    def convert(self):
        try:
            # Validare input
            if not self.amount_entry.get():
                return
                
            amount = float(self.amount_entry.get())
            base = self.from_currency.get()
            target = self.to_currency.get()

            if base == target:
                self.result_label.config(text=f"{amount:.2f} {target}")
                return

            # Apelare API pentru conversie
            url = f"https://api.frankfurter.app/latest?amount={amount}&from={base}&to={target}"
            
            # Folosim un thread si aici pentru a nu bloca butonul
            def run_conversion():
                try:
                    response = requests.get(url)
                    if response.status_code == 200:
                        data = response.json()
                        converted_amount = data['rates'][target]
                        # Update GUI
                        self.root.after(0, lambda: self.result_label.config(text=f"{converted_amount:.2f} {target}"))
                    else:
                        self.root.after(0, lambda: messagebox.showerror("Eroare API", "Nu s-au putut prelua datele."))
                except Exception as e:
                    self.root.after(0, lambda: messagebox.showerror("Eroare", f"Problema conexiune: {e}"))

            threading.Thread(target=run_conversion).start()

        except ValueError:
            messagebox.showwarning("Eroare", "Te rog introdu o suma valida (numar).")

if __name__ == "__main__":
    root = tk.Tk()
    app = CurrencyConverter(root)
    root.mainloop()