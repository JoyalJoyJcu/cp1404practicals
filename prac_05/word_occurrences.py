"""
Word Occurrences
Estimate: 20 minutes
Actual:   35 minutes
"""
user_input = input("write a sentence:")
words = sorted(user_input.split())
word_counts = {}
for word in words:
    word_counts[word] = word_counts.get(word, 0) + 1
width = max(len(word) for word in word_counts.keys())

for word, count in word_counts.items():
    print(f"{word:{width}} : {count}")