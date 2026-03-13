'''
Question 1 – Digital Business Card

Write a program that asks the user to enter the following information:
name
email
phone number
job title
After receiving the input:

Create a dictionary that stores this information
Print the dictionary
Print a formatted business card
Example input:
Enter name: Dana Levi
Enter email: dana@gmail.com
Enter phone: 0501234567
Enter job title: Data Analyst
Possible output:
{'name': 'Dana Levi', 'email': 'dana@gmail.com', 'phone': '0501234567', 'job_title': 'Data Analyst'}

--- Business Card ---
Name: Dana Levi
Email: dana@gmail.com
Phone: 0501234567
Job Title: Data Analyst
'''

RED = '\033[1;31m'
CYAN = '\033[1;36m'
LIME = "\033[93m"
PURPLE = "\033[1;35m"
RESET = '\033[0m'

Business_Card = {}
while True:
        name = str(input(f"{LIME}Enter your name: {RESET}")).title()
        Business_Card['name'] = name
        if name.isdigit() or len(name) <= 0:
            print(f"{RED}Please enter a valid name{RESET}")
            continue
        break
while True:
        email = str(input(f"{LIME}\nEnter your email: {RESET}"))
        Business_Card['email'] = email
        if email.isdigit() or len(email) <= 0:
            print(f"{RED}Please enter a valid email{RESET}")
            continue
        break
while True:
    try:
        phone = int(input(f"{LIME}\nEnter your phone number: {RESET}"))
        Business_Card['phone'] = phone
        break
    except Exception as e:
        print(f"{RED}something went wrong....{RESET}", e )
while True:
        job_title = str(input(f"{LIME}\nEnter your job title: {RESET}")).title()
        Business_Card['job_title'] = job_title
        if job_title.isdigit() or len(job_title) <= 0:
            print(f"{RED}Please enter a valid job title{RESET}")
            continue
        break

print(f"\n{PURPLE}{Business_Card} {RESET}")
print(f"{CYAN}-- Business Card -- {RESET}")
for key, value in Business_Card.items():
    print(f"{CYAN}{key.title()}:{RESET} {value}")