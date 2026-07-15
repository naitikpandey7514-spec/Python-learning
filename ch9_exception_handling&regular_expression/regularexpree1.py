# check if mobile number valid

import re

mobile = input("Enter mobile number: ")

if re.fullmatch(r"\d{10}", mobile):
    print("Valid Mobile Number")
else:
    print("Invalid Mobile Number")