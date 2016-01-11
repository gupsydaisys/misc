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