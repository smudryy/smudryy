import json
import tkinter as tk
from tkinter import messagebox


def load_workers():
    with open("baza.json", encoding="utf-8") as file:
        return json.load(file)


def show_year():
    surname = surname_entry.get().strip()
    year_entry.config(state="normal")
    year_entry.delete(0, tk.END)
    if surname in workers:
        year_entry.insert(0, workers[surname])
    else:
        messagebox.showinfo("Результат", "Працівника з таким прізвищем не знайдено")
    year_entry.config(state="readonly")


def fill_text():
    text.config(state="normal")
    text.delete("1.0", tk.END)
    for surname, year in workers.items():
        text.insert(tk.END, f"{surname} - {year}\n")
    text.config(state="disabled")


workers = load_workers()

root = tk.Tk()
root.title("Співробітники підприємства")
root.geometry("450x350")
root.config(bg="blue")
root.columnconfigure(1, weight=1)
root.rowconfigure(3, weight=1)

tk.Label(root, text="Прізвище:", bg="blue", fg="white").grid(row=0, column=0, padx=10, pady=10, sticky="w")
surname_entry = tk.Entry(root)
surname_entry.grid(row=0, column=1, padx=10, pady=10, sticky="ew")
tk.Button(root, text="Знайти", command=show_year).grid(row=0, column=2, padx=10, pady=10)

tk.Label(root, text="Рік народження:", bg="blue", fg="white").grid(row=1, column=0, padx=10, pady=5, sticky="w")
year_entry = tk.Entry(root, state="readonly")
year_entry.grid(row=1, column=1, padx=10, pady=5, sticky="ew")

tk.Label(root, text="Усі працівники:", bg="blue", fg="white").grid(row=2, column=0, columnspan=3, padx=10, pady=5, sticky="w")
text = tk.Text(root, width=40, height=10)
text.grid(row=3, column=0, columnspan=3, padx=10, pady=(0, 10), sticky="nsew")

fill_text()
root.mainloop()
