import requests
from bs4 import BeautifulSoup
import colorama
from colorama import Fore, Style
colorama.init(autoreset=True)

#! List of classes to check for content in the HTML response
classes = [
    "zCubwf", "hgKElc", "LTKOO sY7ric", "Z0LcW", "gsrt vk_bk FzvWSb YwPhnf", "pclqee", "tw-Data-text tw-text-small tw-ta",
    "IZ6rdc", "O5uR6d LTKOO", "vlzY6d", "webanswers-webanswers_table__webanswers-table",
    "dDoNo ikb4Bb gsrt", "sXLaOe", "LWkfKe", "VQF4g", "qv3Wpe", "kno-rdesc","KAIX8d","PZPZlf","BxUVEf ILfuVd"
]

#! User agent to mimic a browser request
useragent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36'

def online_scraper(query, print_enabled=True):
    """
    #!Function to scrape data from Google search results.
    """
    query = query.replace(" + ", " plus ").replace(" - ", " minus ")  #! Handle URL encodings for symbols
    url = f"https://www.google.co.in/search?q={query}"
    headers = {'User-Agent': useragent}
    page = requests.get(url, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')

    for cls in classes:
        try:
            result = soup.find(class_=cls).get_text()
            result = result.replace('Wikipedia', '').strip()  #! Remove 'Wikipedia' and trim spaces
            if 'Description' in result:
                result = result.replace('Description', 'Description ')  #! Ensure space after 'Description'
            if print_enabled:
                print(f"{Fore.GREEN}Answer found by class {cls}: {Fore.RESET}{result}")
            return result
        except Exception:
            continue

    if print_enabled:
        print(f"{Fore.RED}No answer found for your query.")
    return None

if __name__ == "__main__":
    while True:
        user_input = input("Enter your query or type 'exit' to quit: ")
        if user_input.lower() == "exit":
            print("Exiting the program. Goodbye!")
            break
        answer = online_scraper(user_input, print_enabled=True)
        if answer is None:
            print("Sorry, I couldn't find an answer for your query.")
