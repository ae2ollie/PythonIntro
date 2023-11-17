import requests
from bs4 import BeautifulSoup

# Function to scrape quotes from the website
def scrape_quotes(url):
    # Send a GET request to the URL
    response = requests.get(url)
    
    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the HTML content of the page using BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Extract information (in this case, quotes) from the HTML
        quotes = soup.find_all('span', class_='text')
        
        # Print each quote
        for quote in quotes:
            print(quote.get_text())
    else:
        # Print an error message if the request was not successful
        print(f"Error: Unable to fetch content from {url}")

# URL of the website to scrape
url = "http://quotes.toscrape.com"
# Call the function with the specified URL
scrape_quotes(url)
