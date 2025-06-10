from text_analysis import TextStats
text = input("Input text:\n")
x = TextStats(text)
print("Word count:", x.count_words())
print("Most common letter", x.most_common_letter())
