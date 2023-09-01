import re


def check_password(passw):
    matching_numbers = re.findall('\d', passw)
    digits = [int(n) for n in matching_numbers]
    if len(passw) < 6 or len(passw) > 10:
        print("Password must be between 6 and 10 characters")
    elif passw.isdigit() or passw.isalpha() or not passw.isalnum():
        print("Password must consist only of letters and digits")
    elif len(digits) < 2:
        print("Password must have at least 2 digits")
    else:
        print("Password is valid")


password = input()
check_password(password)
