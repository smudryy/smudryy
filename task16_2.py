import re
import urllib.request

import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator

url = input("Введіть URL-адресу веб-сторінки: ")
request = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
page = urllib.request.urlopen(request, timeout=15).read().decode("utf-8", errors="replace")

levels = ["H1", "H2", "H3", "H4", "H5", "H6"]
counts = [len(re.findall(rf"<h{i}[\s>]", page, flags=re.IGNORECASE)) for i in range(1, 7)]

plt.figure(figsize=(8, 5))
plt.bar(levels, counts)
plt.title("Частота використання заголовків")
plt.xlabel("Рівень заголовка")
plt.ylabel("Кількість")
plt.gca().yaxis.set_major_locator(MaxNLocator(integer=True))
plt.show()
