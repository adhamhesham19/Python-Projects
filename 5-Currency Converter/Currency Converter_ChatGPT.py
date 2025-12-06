import requests

API_KEY = "AhkMo2BA3cb48dQIOrRqPpeuK1gnuO1W"

def get_available_currencies():
    url = "https://api.apilayer.com/fixer/symbols"
    headers = {"apikey": API_KEY}
    response = requests.get(url, headers=headers)
    
    # Check if the request was successful
    if response.status_code == 200:
        data = response.json()
        return data.get("symbols", {})
    else:
        print(f"❌ Error fetching currencies: {response.status_code} - {response.text}")
        return {}

def get_valid_currency(prompt, symbols):
    while True:
        currency = input(prompt).upper().strip()
        if currency in symbols:
            return currency
        print("❌ Invalid currency! Please try again.\n")

def get_valid_amount():
    while True:
        try:
            amount = float(input("Enter amount to convert: "))
            if amount != 0:
                return amount
            print("❌ Amount cannot be 0. Please enter a valid amount.\n")
        except ValueError:
            print("❌ Invalid number. Please try again.\n")

def convert_currency(from_curr, to_curr, amount):
    url = (
        "https://api.apilayer.com/fixer/convert"
        f"?from={from_curr}&to={to_curr}&amount={amount}"
    )
    headers = {"apikey": API_KEY}
    response = requests.get(url, headers=headers)
    
    # Check if the request was successful
    if response.status_code == 200:
        return response.json()
    else:
        print(f"❌ Error during conversion: {response.status_code} - {response.text}")
        return {}

def main():
    print("📘 Fetching available currencies...\n")
    symbols = get_available_currencies()
    
    if not symbols:
        print("❌ Failed to fetch currency symbols. Exiting program.")
        return
    
    # Show full currency list
    print("Available currencies:\n")
    for code, name in symbols.items():
        print(f"{code}: {name}")

    print("\n--- Currency Converter ---\n")
    
    from_curr = get_valid_currency("Enter FROM currency: ", symbols)
    to_curr = get_valid_currency("Enter TO currency: ", symbols)
    amount = get_valid_amount()

    print("\n⏳ Converting...\n")
    result = convert_currency(from_curr, to_curr, amount)

    if result.get("success"):
        converted = result["result"]
        print(f"✅ {amount} {from_curr} = {converted} {to_curr}")
    else:
        print("❌ Conversion failed:", result)

if __name__ == "__main__":
    main()
