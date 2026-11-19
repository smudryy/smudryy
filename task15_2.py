import re
import tkinter as tk
from collections import Counter
from tkinter import messagebox


def find_words():
    try:
        with open("mytext.txt", encoding="utf-8") as file:
            content = file.read()
    except OSError:
        messagebox.showerror("Помилка", "Не вдалося відкрити файл mytext.txt")
        return
    words = re.findall(r"\w+", content.lower())
    top = [word for word, count in Counter(words).most_common(3)]
    top += [""] * (3 - len(top))
    for entry, word in zip(entries, top):
        entry.delete(0, tk.END)
        entry.insert(0, word)


root = tk.Tk()
root.title("Найчастіші слова")
root.geometry("350x230")
root.columnconfigure(0, weight=1)

tk.Label(root, text="Три слова, які найчастіше зустрічаються в тексті:").grid(row=0, column=0, padx=10, pady=10)

entries = []
for i in range(3):
    entry = tk.Entry(root, justify="center")
    entry.grid(row=i + 1, column=0, padx=30, pady=5, sticky="ew")
    entries.append(entry)

tk.Button(root, text="Знайти", command=find_words).grid(row=4, column=0, pady=15)

root.mainloop()
