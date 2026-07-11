#print 1 to 20 number if the number is multiple of 3 print fizz , if the number is multiple of 5 print buzz and if the number is multiple of both then print buzzfizz
for i in range(1,21):
    if i%3 == 0 and i%5 == 0:
        print("buzzfizz")
    elif i%3 == 0:
        print("fizz")
    elif i%5 == 0:
        print("buzz")
    else:
        print(i)