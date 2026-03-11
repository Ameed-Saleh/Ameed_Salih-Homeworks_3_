'''
Write the following Python functions

Function 1
Create a function:

def get_lucky_numbers(amount: int) -> tuple[int]:
    pass
Mission:

Generate a tuple of random numbers
The tuple should contain amount numbers
Each number must be between 1 and 100
Example

get_lucky_numbers(3)
Possible output

(17, 83, 4)
Function 2
Create a function:

def input_until_lucky(lucky_numbers: tuple) -> int:
    pass
Mission:

The function receives the tuple of lucky numbers
Ask the user to input numbers
Continue asking until the user guesses one of the lucky numbers
When the user guesses correctly, stop the loop
Return the number of attempts the user needed
Example

Lucky numbers

(17, 83, 4)
User inputs
10
25
83
Output
3

🚀 Bonus (Optional)
Add try / except:

If the user enters an invalid value (not a number), ask again
The program should not crash
Only valid numeric inputs should count as attempts
'''

import random
RED = '\033[31m'
GREEN = '\033[32m'
CYAN = '\033[36m'
RESET = '\033[0m'

def num_input_validation() -> int:
    while True:
        try:
            _num = int(input(f"{GREEN}enter a number -> {RESET}"))
            return _num
        except Exception as e:
            print(f'{RED}that is not a number{RESET}', e)

def get_lucky_numbers(amount: int) -> tuple:
    '''
    returns tuple of random ints between 1 and 100
    :param amount: how many numbers
    :return: tuple of random ints
    '''
    _result = tuple(random.randint(1, 100) for _ in range(amount))
    print(f"{CYAN}the result = {_result}{RESET}")
    return _result

def input_until_lucky(lucky_numbers: tuple):
    '''
    input numbers from the user until guessed the lucky number
    :param lucky_numbers: the list of lucky numbers
    :return: how many attempts
    '''
    cnt: int = 0
    while True:
        print(f"\n{CYAN}try to guess one of the numbers (1-100)?{RESET}")
        guess: int = num_input_validation()
        cnt += 1
        if guess in lucky_numbers:
            print(f"{GREEN} guess well done bro !{guess} is one of the guesses numbers{RESET}")
            break
        else:
            print(f'{RED}wrong guess, try again{RESET}')

num: int = int(input(f"{CYAN}enter a number that give you the lucky numbers{RESET}"))
lucky = get_lucky_numbers(num)
input_until_lucky(lucky)

