import requests
from bs4 import BeautifulSoup

# Step 1: Target URL
url = "https://python.langchain.com/docs/introduction/"

# Step 2: Send HTTP GET request
response = requests.get(url)

# Step 3: Parse HTML with BeautifulSoup
soup = BeautifulSoup(response.text, 'html.parser')

# Step 4: Extract all anchor tags and their hrefs
links = []
for a_tag in soup.find_all('a', href=True):
    links.append(a_tag['href'])

# Step 5: Print or save the results
for link in links:
    print(link)