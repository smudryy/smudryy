import json
import string
import urllib.request
from html.parser import HTMLParser


class TextExtractor(HTMLParser):
    def __init__(self):
        super().__init__()
        self.parts = []
        self.skip = 0

    def handle_starttag(self, tag, attrs):
        if tag in ("script", "style"):
            self.skip += 1

    def handle_endtag(self, tag):
        if tag in ("script", "style") and self.skip:
            self.skip -= 1

    def handle_data(self, data):
        if not self.skip:
            self.parts.append(data)


def download_page(url):
    request = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(request, timeout=15) as response:
        charset = response.headers.get_content_charset() or "utf-8"
        return response.read().decode(charset, errors="replace")


def count_letters(html):
    extractor = TextExtractor()
    extractor.feed(html)
    text = " ".join(extractor.parts).lower()
    frequency = {letter: 0 for letter in string.ascii_lowercase}
    for char in text:
        if char in frequency:
            frequency[char] += 1
    return frequency


def main():
    url = input("Введіть URL-адресу веб-сторінки: ")
    try:
        html = download_page(url)
    except Exception as error:
        print("Не вдалося завантажити сторінку:", error)
        return
    frequency = count_letters(html)
    with open("letters.json", "w", encoding="utf-8") as file:
        json.dump(frequency, file, ensure_ascii=False, indent=4)
    print("Частоти літер записано у letters.json")


main()
