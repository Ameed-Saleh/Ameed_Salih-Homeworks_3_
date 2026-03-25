'''
7
email
def check_sender(email: str) -> bool:
  pas

stephen.marquard@uct.ac.za

must contain fname + lname seperated by .
must be a . in the name (before the @)
name must be at least 2 letters fname and 2 letetr lname (before the @)
org must be 3 words with 2 dots (after the @)
each word 2 letters at least (after the @)

'''

def check_sender(email: str) -> bool:
    if "@" not in email:
        return False
    name, org = email.split("@")
    if "." not in name:
        return False

    split_name = name.split(".")
    if len(split_name) != 2:
        return False
    for name in split_name:
        if len(name) < 2:
            return False

    split_org = org.split(".")
    if len(split_org) != 3:
        return False
    for word in split_org:
        if len(word) < 2:
            return False

    return True

print(check_sender("stephen.marquard@uct.ac.za"))
print(check_sender("am.salih@org.com"))
print(check_sender("nhs.marquard@uct.co.il"))