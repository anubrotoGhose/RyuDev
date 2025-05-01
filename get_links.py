import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

# Target URL
url = "https://python.langchain.com/docs/introduction/"

# Step 1: Make HTTP GET request
response = requests.get(url)
response.raise_for_status()  # Ensure it fetched successfully

# Step 2: Parse the HTML
soup = BeautifulSoup(response.text, 'html.parser')

# Step 3: Extract and normalize all <a> tag href links
links = set()
for a_tag in soup.find_all('a', href=True):
    full_url = urljoin(url, a_tag['href'])  # Resolve relative URLs
    links.add(full_url)

# Step 4: Print or store links
for link in sorted(links):
    print(link)