# find missing number

all_numbers = set(range(1, 11))
present = {1, 2, 4, 5, 7, 9}

missing = all_numbers - present

print("Missing Numbers:", missing)
