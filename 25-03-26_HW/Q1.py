'''
5
Input: one variable name in camelCase (assume valid camelCase)
Output: the same name converted to snake_case
Example: preferredFirstName → preferred_first_name

def camel_to_snake(name: str) -> str:
  pass
'''

def camel_to_snake(name: str) -> str:
    snake = []
    for letter in name:
        if letter.isupper():
            snake.append('_')
            snake.append(letter.lower())
        else:
            snake.append(letter)
    snake = ''.join(snake)
    return snake


str1 = "preferredFirstName"
print(f"\nstr2: {str1}\nresult: {camel_to_snake(str1)}")


str2 = "HiEtayHowAreYou"
print(f"\nstr2: {str2}\nresult: {camel_to_snake(str2)}")
