'''
🔐 Question 2 – Safe Code
You are given a secret code:

[77, 12, 43, 100, 51]

Goal: the user must enter the numbers exactly in the correct sequence

Rules:

Go through the secret code in order
Each time, the user enters one number
If the number is correct → move to the next number
If the user makes even ONE mistake → reset progress and start again from the beginning
The loop only ends when the full sequence is entered correctly
Example:

4, 10, 77, 12, 43, 77

Explanation:

4 → wrong
10 → wrong
77 → correct (start)
12 → correct
43 → correct
77 → wrong → reset to start
Hint:

Use an index variable to track your position in the code
Reset the index to 0 when there is a mistake
'''

CYAN = '\033[1;36m'
GREEN = "\033[92m"
RED = '\033[1;31m'
RESET = '\033[0m'

def get_user_choice()->int:
    '''
    this function will check if the user enter the  numbers exactly in the correct sequence
    :return: Choice of user's choice
    '''
    while True:
        try:
            choice = int(input(f"{CYAN}enter the secret number💣: {RESET}"))
            break
        except Exception as e:
            print(f"\n{RED}something went wrong....‼️{RESET}", e)
    return choice

def get__sequence_game(numbers1)->int:
    current_index = 0
    while current_index < len(numbers1):
        choice = get_user_choice()
        if choice not in numbers1:
            print(f"\n{RED}wrong ❌{RESET}")
            continue
        if choice == numbers1[current_index]:
            current_index += 1
            if choice == numbers1[0]:
                print(f"\n{GREEN}Correct💥! (start): {current_index}/{len(numbers1)}{RESET}")
            else:
                print(f"\n{GREEN}Correct💥! : {current_index}/{len(numbers1)}{RESET}")
        else:
            current_index = 0
            print(f"\n{RED}wrong ⚠️→ reset to start{RESET}")

    print(f"\n{CYAN}Success✅! You completed the sequence bro💪{RESET}")
    return current_index

_secret_code = [77, 12, 43, 100, 51]
print(f"{CYAN}The Secret Code is -> {RESET}{_secret_code}\n")
get__sequence_game(_secret_code)


