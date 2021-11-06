import requests
from bs4 import BeautifulSoup, NavigableString
import pandas as pd
freq = dict()
url = "https://poligloty.blogspot.com/2018/08/500-samyh-vazhnyh-slov-francuzskogo.html"
response = requests.get(url).text
soup = BeautifulSoup(response, "lxml")
block = soup.find("div", dir="ltr")
words = [x[1:] for x in block.contents if x != '\n' and type(x) == NavigableString]
french_rus = []
for i in words:
    french_rus.append((i[:i.rfind("-")], i[i.rfind("-") + 1:]))
url = "https://www.divelang.ru/blog/useful/30-samykh-trudnoproiznosimykh-slov-na-frantsuzskom-yazyke/"
response = requests.get(url).text
soup = BeautifulSoup(response, "lxml")
block = soup.find("table")
table = block.find("tbody")
cells = table.find_all("tr")
hard_words = []
for i in cells:
    s = i.text
    s = s.replace("\n", "")
    s = s.replace("\t", "")
    s = s.replace("\r", "")
    s = s[3:s.find(" ", 4)] + " " + s[s.rfind("]") + 2:]
    hard_words.append(s)
hard_words.pop(0)
for i in hard_words:
    french_rus.append((i[:i.find(" ", 3)], i[i.find(" ", 3) + 1:]))
df = pd.DataFrame(french_rus, columns=["russian", "french"])
df.to_csv("french_rus.csv", index=False)

