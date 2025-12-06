import requests

init_currency =input("Enter an intial currency: ")
init_target =input("Enter an intial target: ")

while True:
    try:
      amount=float(input("Enter the amount: "))
    except:
       print("The amount must be a numberic value!")
       continue
   
    if amount==0:
       print("The amount must be greater than ")
       continue
    else:
       break
  
url = (f"https://api.apilayer.com/fixer/convert?to={init_target}&from={init_currency}&amount={str(amount)}")

payload = {}
headers= {
  "apikey": "AhkMo2BA3cb48dQIOrRqPpeuK1gnuO1W" 
}

response = requests.request("GET", url, headers=headers, data = payload)

status_code = response.status_code

if(status_code != 200):
   print("Sorry, there was a problem. Please try again later.")
   quit()

result = response.json()
coverted_amount = result['result']

print(F"{amount} {init_currency} = {coverted_amount} {init_target}")

