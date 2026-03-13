'''
Question 2 – Statistics Function

Create a function called:
get_statistics
The function receives a list of numbers and returns a dictionary with the following statistics:

sum
average
minimum
maximum
length of the list
Function structure:

def get_statistics(numbers):
    pass
Demo code:

nums = [4, 8, 2, 10, 6]

result = get_statistics(nums)

print(result)
Possible output:

{
    'sum': 30,
    'avg': 6.0,
    'min': 2,
    'max': 10,
    'length': 5
}
'''
import statistics
import random

def get_random_numbers()-> list:
    '''
    this function will return a list of 5 random numbers
    :return: 5 random numbers at list
    '''
    _numbers = []
    for _ in range(5):
        _numbers.append(random.randint(1, 15))
    print(_numbers)
    return _numbers

def get_statistics(numbers)->dict:
    '''
    this function will return a dictionary with the following statistics:
    :param numbers: the list of numbers
    :return: dictionary with the following statistics
    '''
    _result = {
        'sum': sum(numbers),
        'avg': statistics.mean(numbers),
        'min': min(numbers),
        'max': max(numbers),
        'length': len(numbers)
    }
    return _result

def get_print(_result)->None:
    '''
    this function prints the result
    :param _result: dictionary with the following statistics
    :return: None
    '''
    print(_result)
    for key, value in _result.items():
        print(f'{key}: {value}')

nums = get_random_numbers()
get_statistics(nums)
result = get_statistics(nums)
get_print(result)
