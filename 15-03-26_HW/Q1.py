'''
Exercise 1 – Group words by length
["apple","banana","kiwi","grape","melon","pear"]
-> {
    5: ["apple","grape","melon"],
    6: ["banana"],
    4: ["kiwi","pear"]
}
Write a function that groups words by number of letters

The key should be the length of the word, and the value should be a list of all words with that length
'''
def group_words_by_length(words: list) -> dict:
    '''
    :param words: list of words
    :return: dict { <length>: [list of words with that length] }
    '''
    fruits_dict = {}
    for word in words:
       if len(word) not in fruits_dict:
           fruits_dict[len(word)] = [word]
       else:
           fruits_dict[len(word)].append(word)
    print(f"fruit_dict = {fruits_dict}")
    return fruits_dict

fruits = ["apple","banana","kiwi","grape","melon","pear"]
group_words_by_length(fruits)