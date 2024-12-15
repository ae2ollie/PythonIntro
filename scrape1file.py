import requests
from bs4 import BeautifulSoup

# URL of the website to scrape
url = "https://example.com"

# Send an HTTP GET request to the website
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content of the page
    soup = BeautifulSoup(response.text, "html.parser")
    
    # Extract the desired content (modify as needed)
    # Example: Extract all text on the page
    page_text = soup.get_text()

    # Write the content to a local text file
    with open("website_data.txt", "w", encoding="utf-8") as file:
        file.write(page_text)

    print("Data has been saved to 'website_data.txt'")
else:
    print(f"Failed to retrieve data. HTTP Status Code: {response.status_code}")
