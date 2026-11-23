import json
import re
import urllib.request

titles = {}
for url in open("url.txt", encoding="utf-8").read().split():
    try:
        request = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        page = urllib.request.urlopen(request, timeout=15).read().decode("utf-8", errors="replace")
        titles[url] = " ".join(re.search(r"(?is)<title[^>]*>(.*?)</title>", page).group(1).split())
    except Exception:
        titles[url] = None
with open("title.json", "w", encoding="utf-8") as file:
    json.dump(titles, file, ensure_ascii=False, indent=4)
print("Назви сторінок записано у title.json")