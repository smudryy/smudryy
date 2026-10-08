line1 = input("Enter line 1: ")
line2 = input("Enter line 2: ")
line3 = input("Enter line 3: ")

words1 = set(line1.split())
words2 = set(line2.split())
words3 = set(line3.split())

common_words = words1.intersection(words2, words3)

print("Words common to all three lines:")
if common_words:
  for word in common_words:
    print(word)
else:
  print("No common words found.")
