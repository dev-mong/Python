import requests
from bs4 import BeautifulSoup


def getData():

    result = []
    url = "https://bbs.ruliweb.com/market/board/1020"

    print (" get Data .. ")
    req = requests.get(url)

    html = req.text

    # print(html)

    soup = BeautifulSoup(html, 'html.parser')

    items = soup.select(".subject")
    # print(items)

    for item in items:
        # print(item.text)
        result.append(item.text)

    return result