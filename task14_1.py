import json
import re
import string
import urllib.request
from html import unescape

url = input("Введіть URL-адресу веб-сторінки: ")
request = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
page = urllib.request.urlopen(request, timeout=15).read().decode("utf-8", errors="replace")
page = re.sub(r"(?is)<(script|style).*?</\1>", " ", page)
text = unescape(re.sub(r"<[^>]+>", " ", page)).lower()
frequency = {letter: text.count(letter) for letter in string.ascii_lowercase}
with open("letters.json", "w", encoding="utf-8") as file:
    json.dump(frequency, file, indent=4)
print("Частоти літер записано у letters.json")