import re
import tkinter as tk
from collections import Counter

with open("mytext.txt", encoding="utf-8") as file:
    words = re.findall(r"\w+", file.read().lower())
top = [word for word, count in Counter(words).most_common(3)]

root = tk.Tk()
root.geometry("300x200")

tk.Label(root, text="Найчастіші слова:").grid(row=0, column=0, padx=20, pady=10)
entries = []
for i in range(3):
    entry = tk.Entry(root, justify="center")
    entry.grid(row=i + 1, column=0, padx=20, pady=5)
    entries.append(entry)
tk.Button(
    root,
    text="Знайти",
    command=lambda: [
        (e.delete(0, tk.END), e.insert(0, w))
        for e, w in zip(entries, top)
    ],
).grid(row=4, column=0, pady=10)

root.mainloop()