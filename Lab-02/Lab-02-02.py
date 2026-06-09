def split(s):
    mid = (len(s) + 1) // 2
    front_half = s[:mid]
    back_half = s[mid:]
    return front_half, back_half

s = "lorem ipsum"
front, back = split(s)

def combine(a, b):
    a_front, a_back = split(a)
    b_front, b_back = split(b)
    return a_front + b_front + a_back + b_back

a = "lorem"
b = "ipsum"
print(combine(a, b))
