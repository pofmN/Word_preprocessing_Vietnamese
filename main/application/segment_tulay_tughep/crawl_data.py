import requests
from bs4 import BeautifulSoup

url = "https://vi.wiktionary.org/wiki/Th%E1%BB%83_lo%E1%BA%A1i:T%E1%BB%AB_gh%C3%A9p_trong_ti%E1%BA%BFng_Vi%E1%BB%87t"
response = requests.get(url)

soup = BeautifulSoup(response.content, "html.parser")
li_tags = soup.find_all("li")

for li in li_tags:
    a_tag = li.find("a")
    if a_tag:
        data = a_tag.text
        print(data+", ")
