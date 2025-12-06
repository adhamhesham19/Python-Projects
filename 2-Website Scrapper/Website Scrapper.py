import requests 
from bs4 import BeautifulSoup

reponse = requests.get("https://books.toscrape.com/")


soup= BeautifulSoup(reponse.content ,"html.parser")

books =soup.find_all("article")

for book in books:
    title= book.h3.a["title"]
    rating=book.p["class"][1]
    price = book.find("p", class_="price_color").text
    print(f"Book title:{title} | Has rating: {rating} | stars  it's price: {price}")