# Reverse digits of an integer.
# Example1: x = 123, return 321
# Example2: x = -123, return -321

def reverseDigits(x):
    if x == 0:
        return 0
    isNeg = True if x < 0 else False
    x = -x if isNeg else x
    str0 = ""
    while (x != 0):
        n = x % 10
        str0 = str0 + str(n)
        x = (x - n) / 10
    # print str0
    str0 = int(str0)
    return -str0 if isNeg else str0

# don't use an extra string
def reverseDigits(x):
    if x == 0:
        return 0
    isNeg = True if x < 0 else False
    x = -x if isNeg else x
    out = 0
    while (x != 0):
        digit = x % 10
        out = out*10 + digit
        x = (x - digit) / 10
    return -out if isNeg else out

assert reverseDigits(0) == 0
assert reverseDigits(123) == 321
assert reverseDigits(-123) == -321
assert reverseDigits(1234) == 4321
assert reverseDigits(-1234) == -4321