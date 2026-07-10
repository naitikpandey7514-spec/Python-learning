#write a program take a user element and make it in ascending and descending order


num = {"a" :10 , "c":20 , "b":15, "d":25}
#ascending
ascen = dict(sorted(num.items()))
print("dictionary in ascending order:",ascen)
#descending
descen = dict(sorted(num.items(),reverse=True))
print("dictionary in descending order:",descen)