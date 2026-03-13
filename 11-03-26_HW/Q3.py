'''
Question 3 – Bonus - Merge Two Dictionaries
Create a function that receives two dictionaries.
Each dictionary has:
key → string
value → string
The function should create and return a third dictionary that combines both dictionaries.

Rules:
If a key appears in only one dictionary, add it normally
If the same key appears in both dictionaries, choose the value with the longer string
If both strings have the same length, keep the value from the first dictionary
Example:
dict1 = {
    "name": "Dan",
    "city": "Tel Aviv",
    "job": "Dev"
}

dict2 = {
    "name": "Daniel",
    "city": "TA",
    "country": "Israel"
}

Possible result:
{
    "name": "Daniel",
    "city": "Tel Aviv",
    "job": "Dev",
    "country": "Israel"
}
'''

def get_new_dict(dict1, dict2)-> dict[str, str]:
    '''
    this function will return a third dictionary that combines both dictionaries
    :param dict1: contains dict_one
    :param dict2: contains dict_two
    :return: the third dictionary that combines both dictionaries
    '''
    dict_three = dict1.copy()
    for key, value2 in dict2.items():
        if key in dict_three:
            value1 = dict_three[key]
            if len(value2) > len(value1):
                dict_three[key] = value2
        else:
            dict_three[key] = value2
    print(dict_three)
    return dict_three

dict_one = {
    "name": "Ameed salih",
    "city": "Maghar",
    "job": "Ai",
}

dict_two = {
    "name": "Daniel",
    "city": "Tel Aviv",
    "job": "Police",
    "country": "Israel"
}
get_new_dict(dict_one, dict_two)
