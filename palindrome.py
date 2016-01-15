import math

#####################################################################################
# A palindromic number reads the same both ways. The largest palindrome
# made from the product of two 2-digit numbers is 9009 = 91 × 99. What 
# is the largest palindrome made from the product of two 3-digit numbers?
#####################################################################################

def isPalindrome(n):
    string = str(n)
    last = len(string) - 1
    mdpt = int(math.ceil(len(string) / 2.0))
    for i in range(mdpt):
        if (string[i] is not string[last - i]):
            return False
    return True

def isP(str):
    for i in range(len(str)/2):
        if str[i] != str[-1-i]:
            return False
    return True

assert isP("") == True
assert isP("h") == True
assert isP("heh") == True
assert isP("hhhh") == True
assert isP("hellolleh") == True
assert isP("hellollh") == False
assert isP("hellolle") == False
assert isP("hello") == False


def getPalindrome():
    m = -1;
    i = 999
    while (i > 99):
        j = 999
        while (j > 99):
            prod = i*j;
            if isPalindrome(prod) and prod > m:
                m = prod
            j -= 1
        i -= 1
    return m

getPalindrome()

# Determine whether an integer is a palindrome. Do this without extra space.

def getLen(n):
    k = 1
    while (n / 10**k != 0):
        k += 1
    return k

assert getLen(10) == 2
assert getLen(0) == 1
assert getLen(1) == 1
assert getLen(500) == 3
assert getLen(9999) == 4

def getKthDigit(n, k):
    # 191 - (191 % 1) / 1 % 10 -> 1st digit
    # 191 - (191 % 10) / 10 % 10 -> 2cd digit
    # 191 - 191 % 100 / 100 % 10 -> 3rd digit
    p = 10**k
    t = n % p
    out = n - t
    out = out / p
    out = out % 10
    return out

assert getKthDigit(391, 0) == 1
assert getKthDigit(391, 1) == 9
assert getKthDigit(391, 2) == 3
assert getKthDigit(3915, 2) == 9

def isIntPalindrome(n):
    if n < 0:
        return False;
    l = getLen(n)
    for i in range(l/2):
        if getKthDigit(n, i) != getKthDigit(n, l - 1 - i):
            return False
    return True
    
assert isIntPalindrome(-1) == False
assert isIntPalindrome(0) == True
assert isIntPalindrome(191) == True
assert isIntPalindrome(1991) == True
assert isIntPalindrome(1981) == False
assert isIntPalindrome(1992) == False
assert isIntPalindrome(199) == False