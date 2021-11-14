import requests
from bs4 import BeautifulSoup
from math import inf
import pandas as pd

freq = dict()

url = "https://icaltefl.com/word-frequency/"
response = requests.get(url)
soup = BeautifulSoup(response.content, "lxml")
table = soup.find('tbody')
arr = table.findAll('tr')
for elem in arr[1:]:
    arr2 = elem.findAll('td')
    freq[arr2[1].text] = int(arr2[0].text)

eng_rus_vocabulary = []

url = "https://studynow.ru/dicta/allwords"
response = requests.get(url)
soup = BeautifulSoup(response.content, "lxml")
table = soup.find(id="wordlist")
arr = table.findAll('tr')
for elem in arr:
    arr2 = elem.findAll('td')
    eng_rus_vocabulary.append((arr2[1].text, arr2[2].text, freq.get(arr2[1].text, inf)))
eng_rus_vocabulary.sort(key=lambda x : x[2])
df = pd.DataFrame(eng_rus_vocabulary, columns=["english", "russian", "freq"])
df.drop("freq", axis=1, inplace=True)
df.to_csv("eng_rus.csv", index=False)
