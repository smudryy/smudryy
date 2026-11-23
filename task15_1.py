import json
import tkinter as tk

with open("baza.json", encoding="utf-8") as file:
    workers = json.load(file)

root = tk.Tk()
root.geometry("450x350")
root.config(bg="blue")

tk.Label(root, text="Прізвище:", bg="blue", fg="white").grid(row=0, column=0, padx=5, pady=5)
name = tk.Entry(root)
name.grid(row=0, column=1, padx=5, pady=5)
tk.Label(root, text="Рік народження:", bg="blue", fg="white").grid(row=1, column=0, padx=5, pady=5)
year = tk.Entry(root)
year.grid(row=1, column=1, padx=5, pady=5)
tk.Button(
    root,
    text="Знайти",
    command=lambda: (
        year.delete(0, tk.END),
        year.insert(0, workers.get(name.get().strip(), "не знайдено")),
    ),
).grid(row=0, column=2, padx=5, pady=5)

text = tk.Text(root, width=50, height=12)
text.grid(row=2, column=0, columnspan=3, padx=5, pady=5)
for surname, born in workers.items():
    text.insert(tk.END, f"{surname} - {born}\n")

root.mainloop()