words = ["hello", "morning", "over", "to"]
sorted_words = sorted(words, key=lambda x: (len(x), x))
print(sorted_words)