import json
import urllib.request
from html.parser import HTMLParser


class TitleParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.in_title = False
        self.title = ""

    def handle_starttag(self, tag, attrs):
        if tag == "title":
            self.in_title = True

    def handle_endtag(self, tag):
        if tag == "title":
            self.in_title = False

    def handle_data(self, data):
        if self.in_title:
            self.title += data


def download_page(url):
    request = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(request, timeout=15) as response:
        charset = response.headers.get_content_charset() or "utf-8"
        return response.read().decode(charset, errors="replace")


def get_title(url):
    parser = TitleParser()
    parser.feed(download_page(url))
    return " ".join(parser.title.split())


def main():
    with open("url.txt", encoding="utf-8") as file:
        urls = [line.strip() for line in file if line.strip()]
    titles = {}
    for url in urls:
        try:
            titles[url] = get_title(url)
        except Exception as error:
            titles[url] = None
            print("Помилка для", url, "-", error)
    with open("title.json", "w", encoding="utf-8") as file:
        json.dump(titles, file, ensure_ascii=False, indent=4)
    print("Назви сторінок записано у title.json")


main()
