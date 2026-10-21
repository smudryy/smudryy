# Множина з 7-10 ключових слів сайту
keywords = {
    "programming", "python", "website", "database",
    "network", "server", "algorithm", "browser"
}

def remove_repeating(word):
    """Удаляет из слова все символы, которые в нём повторяются."""
    seen_once = set()      # символы, встретившиеся хотя бы раз
    repeated = set()       # символы, встретившиеся 2+ раз
    for ch in word:
        if ch in seen_once:
            repeated.add(ch)
        seen_once.add(ch)
    unique_only = seen_once - repeated   # разность множеств
    return "".join(ch for ch in word if ch in unique_only)

# Проверка размера множества
if not 7 <= len(keywords) <= 10:
    print("Множина повинна містити 7-10 слів!")
else:
    result = {remove_repeating(w) for w in keywords}
    print("Було: ", sorted(keywords))
    print("Стало:", sorted(result))