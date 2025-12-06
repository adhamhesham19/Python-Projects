import requests
from bs4 import BeautifulSoup

# URL of the website to scrape
url = 'https://books.toscrape.com/'

# Send a GET request to fetch the page content
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find all book containers on the page
    books = soup.find_all('article', class_='product_pod')

    # Loop through each book and extract the relevant information
    for book in books:
        title = book.find('h3').find('a')['title']  # Extract book title
        price = book.find('p', class_='price_color').text  # Extract book price
        rating = book.find('p', class_='star-rating')['class'][1]  # Extract rating class

        # Print the extracted information
        print(f"Title: {title}")
        print(f"Price: {price}")
        print(f"Rating: {rating}")
        print('-' * 30)  # Print a separator between books
else:
    print(f"Failed to retrieve the page. Status code: {response.status_code}")
