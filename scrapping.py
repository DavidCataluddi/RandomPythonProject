import requests
from bs4 import BeautifulSoup

def sending_request(page_url):
    r = requests.get(page_url)
    if r.status_code == 200:
        print(r.status_code)
        return r
    else:
        exit(0)

def getting_result(r):
    soup = BeautifulSoup(r.text, "html.parser")
    quotes = soup.find_all("div", class_="quote")

    for quote in quotes:
        text = quote.find("span", class_="text").get_text()
        author = quote.find("small", class_="author").get_text()
        taglist = []
        for tag in quote.find_all("a", class_="tag"):
            tags = taglist.append(tag.get_text())

        print(f"Quote: {text}")
        print(f"Author: {author}")
        print(f"Tags: {', '.join(taglist)}")
        print("-"*24)

def main():
    r = sending_request('https://quotes.toscrape.com/')
    getting_result(r)


if __name__ == '__main__':
    main()