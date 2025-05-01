import sqlite3
import requests
from dotenv import load_dotenv
from bs4 import BeautifulSoup
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

llm = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash",
    temperature=0,
    max_tokens=None,
    timeout=None,
    max_retries=2,
)

def desc_of_the_url(url):
    try:
        # Step 1: Fetch the content of the URL
        response = requests.get(url, timeout=10)
        response.raise_for_status()  # Raise error for bad status codes

        # Step 2: Parse the HTML with BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Step 3: Extract relevant text
        for script_or_style in soup(["script", "style", "noscript"]):
            script_or_style.decompose()  # Remove unwanted tags
        text = soup.get_text(separator=' ', strip=True)

        # Optionally truncate the text to avoid token limits
        cleaned_text = text[:8000]  # You can adjust based on the model's context length

        # Step 4: Create prompt for LLM
        prompt = (
            "Please read the following web content and generate a detailed summary "
            "focused on programming or software development topics mentioned:\n\n"
            f"{cleaned_text}"
        )

        # Step 5: Call the LLM to generate the summary
        response = llm.invoke(prompt)
        return response

    except Exception as e:
        return f"An error occurred: {e}"



def desc__of_link_into_db(db_path='data/programming_knowledge_hub.sqlite3'):

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


if __name__ == "__main__":

    url = "https://realpython.com/python-web-scraping-practical-introduction/"
    summary = desc_of_the_url(url)
    print(summary)