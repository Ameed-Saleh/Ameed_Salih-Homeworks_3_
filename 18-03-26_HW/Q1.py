'''
Question 1 – N-th Biggest Number
Write a function that gets:

A list of numbers (with duplicates)
A number n
The function should return the n-th biggest unique number in the list

Example:

[88, 100, 90, 95, 95, 97, 97, 99, 97, 99] , n = 4

Result:
95

Explanation:
Unique sorted values (descending):

100, 99, 97, 95, 90, 88

The 4th biggest number is 95

Rules:

Ignore duplicates when counting
Assume n is valid (you don’t need to handle errors)
'''

RED = '\033[1;31m'
CYAN = '\033[1;36m'
PURPLE = "\033[1;35m"
RESET = '\033[0m'
def get_biggest(numbers)->int | bool:
    '''
    this function is used to find the n-th biggest number in the list of numbers
    :param numbers: List of numbers
    :return: The biggest number, and return False if there is no biggest number
    '''
    numbers1 = set(numbers)
    numbers2 = []
    while True:
        try:
            n = int(input(f"{PURPLE}enter n: {RESET}"))
            break
        except Exception as e:
            print(f"\n{RED}something went wrong....{RESET}", e)
    choice = 0
    while True:
        choice += 1
        n -= 1
        if n == 0:
            break
        try:
            numbers2.append(max(numbers1))
            numbers1.remove(max(numbers1))
            continue
        except ValueError:
            break
    try:
        print(f"\n{CYAN}the biggest number is {RESET}{max(numbers1)}")
        print(f"{CYAN}because it is the {choice}-th biggest after {RESET}{numbers2}")
        return max(numbers1)
    except Exception as e:
        print(f"\n{RED}something went wrong....{RESET}" , e)
        return False

list1 = [88, 100, 90, 95, 95, 97, 97, 99, 97, 99]
print(f"\n{PURPLE}list1: {list1}{RESET}")
get_biggest(list1)
list2 = [90, 100, 94]
print(f"\n{PURPLE}list2: {list2}{RESET}")
get_biggest(list2)
list3 = [90, 100, 94, 98]
print(f"\n{PURPLE}list3: {list3}{RESET}")
get_biggest(list3)