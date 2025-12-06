import tkinter as tk
from tkinter import messagebox
import requests

# Your Apilayer API key
API_KEY = "AhkMo2BA3cb48dQIOrRqPpeuK1gnuO1W"

# Fetch available currencies
def get_available_currencies():
    url = "https://api.apilayer.com/fixer/symbols"
    headers = {"apikey": API_KEY}
    response = requests.get(url, headers=headers)
    data = response.json()
    return data.get("symbols", {})

# Convert currency
def convert_currency(from_curr, to_curr, amount):
    url = f"https://api.apilayer.com/fixer/convert?from={from_curr}&to={to_curr}&amount={amount}"
    headers = {"apikey": API_KEY}
    response = requests.get(url, headers=headers)
    return response.json()

# Trigger the conversion
def on_convert():
    from_curr = from_currency.get()
    to_curr = to_currency.get()
    amount = amount_entry.get()

    # Validation for amount
    try:
        amount = float(amount)
        if amount <= 0:
            messagebox.showerror("Invalid Amount", "Amount must be greater than 0.")
            return
    except ValueError:
        messagebox.showerror("Invalid Amount", "Please enter a valid number for amount.")
        return

    # Convert the currency
    result = convert_currency(from_curr, to_curr, amount)
    
    if result.get("success"):
        converted_amount = result["result"]
        result_label.config(text=f"✅ {amount} {from_curr} = {converted_amount:.2f} {to_curr}")
    else:
        messagebox.showerror("Error", "Conversion failed. Please try again.")

# Setup Tkinter window
root = tk.Tk()
root.title("Currency Converter")
root.geometry("400x300")

# Fetch available currencies for dropdowns
currencies = get_available_currencies()
currency_codes = list(currencies.keys())

# From Currency Dropdown
from_currency_label = tk.Label(root, text="From Currency:")
from_currency_label.pack(pady=5)
from_currency = tk.StringVar()
from_currency.set(currency_codes[0])  # Default currency
from_currency_menu = tk.OptionMenu(root, from_currency, *currency_codes)
from_currency_menu.pack(pady=5)

# To Currency Dropdown
to_currency_label = tk.Label(root, text="To Currency:")
to_currency_label.pack(pady=5)
to_currency = tk.StringVar()
to_currency.set(currency_codes[1])  # Default currency
to_currency_menu = tk.OptionMenu(root, to_currency, *currency_codes)
to_currency_menu.pack(pady=5)

# Amount Entry
amount_label = tk.Label(root, text="Amount:")
amount_label.pack(pady=5)
amount_entry = tk.Entry(root)
amount_entry.pack(pady=5)

# Convert Button
convert_button = tk.Button(root, text="Convert", command=on_convert)
convert_button.pack(pady=10)

# Result Label
result_label = tk.Label(root, text="Converted Amount will appear here.")
result_label.pack(pady=10)

# Start the Tkinter main loop
root.mainloop()
