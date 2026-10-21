import re
from collections import Counter

# Читаем текст
with open("story.txt", "r", encoding="utf-8") as f:
    text = f.read()

# 1) Слова: последовательности букв (апостроф учитываем, например don't)
words = re.findall(r"[A-Za-z']+", text.lower())
word_count = len(words)

# 2) Предложения: делим по . ! ? и отбрасываем пустые куски
sentences = [s for s in re.split(r"[.!?]+", text) if s.strip()]
sentence_count = len(sentences)

# 3) 4 самых частых слова
top4 = Counter(words).most_common(4)

# Вывод на экран
print("Слів:", word_count)
print("Речень:", sentence_count)
print("Найчастіші слова:")
for word, count in top4:
    print(f"  {word}: {count}")

# 4) Сохраняем результаты в отдельные файлы
with open("word_count.txt", "w", encoding="utf-8") as f:
    f.write(str(word_count))

with open("sentence_count.txt", "w", encoding="utf-8") as f:
    f.write(str(sentence_count))

with open("top_words.txt", "w", encoding="utf-8") as f:
    for word, count in top4:
        f.write(f"{word}: {count}\n")