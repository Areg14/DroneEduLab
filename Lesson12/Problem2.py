words = []
word_lengths = []
for i in range(7):
    word = input()
    words.append(word)


for word in words:
    word_lengths.append(len(word))

max_length_word = max(word_lengths)

for i, n in zip(words, word_lengths):
    if n == max_length_word:
        print(f"{i} is the largest word!")