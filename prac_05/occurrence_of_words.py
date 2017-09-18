"""
CP1404/CP5632 Practical
Count same words from input
"""
counted_words = {}
text = input("Text: ")
text = text.split()

for word in text:
    if word in counted_words:
        counted_words[word] += 1
    else:
        counted_words[word] = 1

sorted_words = list(counted_words.keys())
sorted_words.sort()
longest_word = max(len(word) for word in counted_words)

for word in sorted_words:
    print("{:<{}} : {}".format(word, longest_word, counted_words[word]))
