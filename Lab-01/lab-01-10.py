s = input("enter something: ")
digits = 0
letters = 0
for c in s:
    if c.isdigit():
        digits += 1
    elif c.isalpha():
        letters += 1
print("digits:", digits)
print("letters:", letters)