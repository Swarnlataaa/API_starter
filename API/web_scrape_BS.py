import requests
from bs4 import BeautifulSoup

# Define the URL of the website to scrape
url = 'https://example.com/articles'

# Send an HTTP GET request to the website
response = requests.get(url)

# Parse the HTML content of the page using BeautifulSoup
soup = BeautifulSoup(response.text, 'html.parser')

# Find and extract article titles (assuming they are in <h2> tags)
titles = [title.text for title in soup.find_all('h2')]

# Print the titles
for title in titles:
    print(title)
