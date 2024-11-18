import urllib.request, os
from bs4 import BeautifulSoup

url = "https://www.bestbuy.ca/en-ca/category/ps4-games/33934"
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36"}
req = urllib.request.Request(url, headers=headers)
webUrl = urllib.request.urlopen(req)

data = webUrl.read()

soup = BeautifulSoup(data, 'html.parser')

titles = soup.find_all(class_='productItemName_3IZ3c')

for i, title in enumerate(titles, start=1):
    textFile = open("E:\\Projects\\ps4WebScraper\\gameTitle.txt", "a")
    textFile.write(f"{i}. {title.get_text(strip=True)} \n")
    textFile.close()

