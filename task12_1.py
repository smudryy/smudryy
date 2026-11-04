def pad_words(text):
    words = text.split()
    if not words:
        return ""
    result = " ".join(words)
    extra = (-len(result)) % 4
    spaces = [0] * len(words)
    for i in range(extra):
        spaces[i % len(words)] += 1
    parts = []
    for i, word in enumerate(words):
        parts.append(word + " " * spaces[i])
        if i < len(words) - 1:
            parts.append(" ")
    return "".join(parts)


def first_and_last(text):
    words = text.split()
    if not words:
        return None, None
    return words[0], words[-1]


def main():
    text = input("Введіть рядок: ")
    padded = pad_words(text)
    for i in range(0, len(padded), 4):
        print(padded[i:i + 4])
    first, last = first_and_last(text)
    if first is None:
        print("Рядок не містить слів")
    else:
        print("Перше слово:", first)
        print("Останнє слово:", last)


main()
