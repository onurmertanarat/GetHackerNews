import requests
from bs4 import BeautifulSoup

target_url = "https://news.ycombinator.com/"
rsp = requests.get(target_url)

# print(rsp.text)

soup = BeautifulSoup(rsp.text, "html.parser")

titles = soup.find_all('span', class_="titleline")

title_array = []

for title in titles:
    # print(title.text)
    title_array.append(title.text)

# print(title_array)

for title in title_array:
    print(title)

