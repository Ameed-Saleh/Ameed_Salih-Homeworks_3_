'''
Exercise 7
["apple","banana","avocado","blueberry","apricot","corn"]

-> {
    "a": ["apple","avocado","apricot"],
    "b": ["banana","blueberry"],
    "c": ["corn"]
}
'''
def group_by_letter(words: list) -> dict:
    '''
    :param words: list of words
    :return: dictionary where:
             key = first letter of the word
             value = list of all words that start with that letter
    '''
    fruits_dict = {}
    for word in words:
        if word[0] not in fruits_dict:
            fruits_dict[word[0]] = [word]
        else:
            fruits_dict[word[0]].append(word)
    print(f"Question-7 = {fruits_dict}")
    return fruits_dict

fruits = ["apple","banana","avocado","blueberry","apricot","corn" ]
group_by_letter(fruits)