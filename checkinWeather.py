from bs4 import BeautifulSoup
import requests

def getWeather(city):
    url = "https://www.google.com/search?q=" + city + " weather"
    html = requests.get(url).content

    soup = BeautifulSoup(html, 'html.parser')
    temp = soup.find('div', attrs={'class': 'BNeawe iBp4i AP7Wnd'}).text
    data = soup.find('div', attrs={'class': 'BNeawe tAd8D AP7Wnd'}).text

    desc = data.split('\n')[1]
    return desc


if __name__ == '__main__':
    print(getWeather('Mumbai'))