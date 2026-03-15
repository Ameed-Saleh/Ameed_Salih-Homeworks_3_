'''
Exercise 3 – Group numbers by sign
[4, -2, 0, 7, -5, 3]

-> {
    "positive": [4,7,3],
    "negative": [-2,-5],
    "zero": [0]
}
Write a function that groups numbers based on their sign
'''

def group_numbers(nums: list) -> dict:
    '''
    :param nums: list of numbers
    :return: dictionary with keys:
             "positive", "negative", "zero"
             and lists of numbers for each category
    '''
    numbers_dict ={ "positive": [], "negative": [], "zero": []}
    for num in nums:
        if num > 0:
            numbers_dict["positive"].append(num)
        elif num < 0:
            numbers_dict["negative"].append(num)
        else:
            numbers_dict["zero"].append(num)
    print(f"numbers_dict = {numbers_dict}")
    return numbers_dict

numbers = [4, -2, 0, 7, -5, 3]
group_numbers(numbers)