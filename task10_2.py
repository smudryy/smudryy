import os

# Каталог Program Files
program_files = os.environ.get("ProgramFiles", r"C:\Program Files")

print("Вміст каталогу", program_files)
for name in os.listdir(program_files):
    print(" ", name)

# Каталог Windows
windows_dir = os.environ.get("SystemRoot", r"C:\Windows")

with open("w.txt", "w", encoding="utf-8") as f:
    for name in os.listdir(windows_dir):
        full_path = os.path.join(windows_dir, name)
        if os.path.isfile(full_path):      # только файлы, без папок
            f.write(name + "\n")

print("Імена файлів з", windows_dir, "записано у w.txt")