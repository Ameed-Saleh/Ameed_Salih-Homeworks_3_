'''
6
Write a function word_frequencies(text) that returns a dictionary mapping
each word (lowercased) to the number of times it appears
Assume words are separated by whitespace

Example: "To be or not to be" → {"to": 2, "be": 2, "or": 1, "not": 1}
def count_freq(sentence: str) -> dict[str, int]:
  pass
'''
def count_freq(sentence: str) -> dict[str, int]:
    dict1 = {}
    sentence = sentence.lower()
    for word in sentence.split():
        if word not in dict1:
            dict1[word] = 1
        else:
            dict1[word] += 1
    return dict1

text1 = "To be or not to be"
print(f"\ntext1: {text1}\nresult: {count_freq(text1)}")

text2 = "To be or not to be To Be Not or Or be"
print(f"\ntext2: {text2}\nresult: {count_freq(text2)}")
