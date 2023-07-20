import requests
from bs4 import BeautifulSoup

def web_scraper():
    url = "https://example.com"  # Replace this with the URL of the website you want to scrape

    try:
        response = requests.get(url)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, "html.parser")

        # Example: Extracting the page title
        page_title = soup.title.text.strip()
        print("Page Title:", page_title)

        # Example: Extracting all links from the page
        links = soup.find_all("a")
        print("\nLinks on the Page:")
        for link in links:
            print(link["href"])

        # Example: Extracting specific data from the page
        # Replace this part with the relevant tags and attributes of the data you want to scrape
        data_elements = soup.find_all("div", class_="data-item")
        print("\nData Items:")
        for element in data_elements:
            data = element.text.strip()
            print(data)

    except requests.exceptions.RequestException as e:
        print("Error connecting to the website:", e)

if __name__ == "__main__":
    web_scraper()
