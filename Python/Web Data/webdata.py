import requests
from bs4 import BeautifulSoup

url = 'https://www.ssb.no'
url_name = 'https://www.ssb.no/befolkning/navn/statistikk/navn'

response = requests.get(url)
response_name = requests.get(url_name)

access_input: str = input("Hvilke data vil du se?   ")

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find all <div> elements with the class "content"
    web_pop_stats = soup.find_all('div', class_='ssb-number small')


    # Extract and print the text of each content div
    for stat in web_pop_stats:
        print(stat.text)

if response.status_code == 200 & access_input == "Navn":
    soup = BeautifulSoup(response.text, 'html.parser')

    web_name_stats = soup.find_all('p')
    print(web_name_stats)

# Error message
else:
    print(f"Failed to retrieve the page. Status code: {response.status_code}")