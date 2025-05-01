import sqlite3
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import numpy as np

def qet_links_from_url(url):

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

    return links

def post_link_into_db(db_path='data/programming_knowledge_hub.sqlite3'):

    connection_obj = sqlite3.connect(db_path)

    cursor_obj = connection_obj.cursor() 

    sql_query = '''SELECT Links FROM websites'''

    cursor_obj.execute(sql_query)

    output = cursor_obj.fetchall() 
    links = set()
    for row in output:
        # print(row[0])
        if row[0] is not None:
            links.update(qet_links_from_url(row[0]))


    connection_obj.commit()

    connection_obj.close()

    return links

if __name__ == "__main__":
    links = post_link_into_db(db_path='data/programming_knowledge_hub.sqlite3')
    np_links = np.array(list(links))
    print(np_links)
    print(np_links.shape)