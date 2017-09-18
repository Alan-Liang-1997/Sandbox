"""
CP1404/CP5632 Practical
Count same words from input
"""
counted_words = {}
text = input("Text: ")

for word in text.split():
    try:
        counted_words[word] += 1
    except:
        counted_words[word] = 1
longest_word = max(len(word) for word in counted_words)


for word, word_count in sorted(counted_words.items()):
    print("{:<{}} : {}".format(word, longest_word, counted_words[word]))
