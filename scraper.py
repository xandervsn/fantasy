import requests
from bs4 import BeautifulSoup

def scrape():
    
    url = 'https://www.maxpreps.com/or/medford/south-medford-panthers/athletes/kameron-rague/?careerid=8agtqssn8gnbb'
    response = requests.get(url)
    soup = str(BeautifulSoup(response.text, 'html.parser'))
    arr = soup.split("Rushing Yards")
    arr[0]

if __name__ == '__main__':
    scrape()
