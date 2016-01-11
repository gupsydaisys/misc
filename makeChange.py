#####################################################################################
# The problem of determining the number of combos of 2, 3, 7
# point plays that can generate a socre of 222
#####################################################################################

# Where order does matter like in football to count the number
# of combinations of 2, 3, 7 point plays can end with a score
# of 222

# Runtime is o(number_of_denoms^(n/smallest_denom))
def getPerms(n):
    if (n == 0):
        return 1
    else:
        s = 0
        if (n >= 7):
            s += getPerms(n - 7)
        if (n >= 3):
            s += getPerms(n - 3)
        if (n >= 2):
            s += getPerms(n - 2)
        return s

# Use a table to look up previously computed values,
# Runtime is still bad since you hae to iteratre through all of them
hMap = {}
hMap[0] = 1
def getPerms2(n, hMap):
    if (n in hMap):
        return hMap[n]
    else:
        s = 0
        if (n >= 7):
            s += getPerms(n - 7)
        if (n >= 3):
            s += getPerms(n - 3)
        if (n >= 2):
            s += getPerms(n - 2)
        hMap[n] = s
        return s

# Use a table to look up previously computed values and iteratively calculate
# them from the ground up
# Runtime is o(n)
def getPerms3(n, denoms):
    lst = [0 for i in range(n+1)]
    lst[0] = 1
    for i in range(1, n+1):
        for d in denoms:
            diff = i - d
            lst[i] += 0 if (diff < 0) else lst[diff]
    return lst[n]

# Use a table to look up previously computed values and RECURSIVELY calculate
# them from the ground up
# Runtime is o(n)
def getPerms4(n, denoms):
    lst = [-1 for i in range(n+1)]
    lst[0] = 1
    return getPerms4Helper(n, denoms, lst)[-1]

def getPerms4Helper(i, denoms, lst):
    if lst[i] != -1:
        return lst
    else:
        lst[i] = 0
        for d in denoms:
            diff = i - d
            if diff >= 0:
                lst = getPerms4Helper(diff, denoms, lst)
                lst[i] += lst[diff]
        return lst

# Use a table to look up previously computed values and RECURSIVELY calculate
# them from the ground up
# Runtime is o(n)
def getPerms4(n, denoms):
    lst = [-1 for i in range(n+1)]
    lst[0] = 1
    return getPerms4Helper(n, denoms, lst)[-1]

def getPerms4Helper(i, denoms, lst):
    if lst[i] != -1:
        return lst
    else:
        lst[i] = 0
        for d in denoms:
            diff = i - d
            if diff >= 0:
                lst = getPerms4Helper(diff, denoms, lst)
                lst[i] += lst[diff]
        return lst

# Where order does NOT matter like counting # of
# ways to get 222 from 2, 3, 7
def getCombos(n, denoms):
    if (n == 0):
        return 1
    elif (n < 0):
        return 0;
    else:
        s = 0
        if len(denoms) > 0:
            i = 0
            while (i * denoms[0] <= n):
                s += getCombos(n - i*denoms[0], denoms[1:])
                i += 1
        return s

import sys

# how can a given amount of money be made with the least number of coins of given denominations
# o(n^denoms)
def getMinChange(n, denoms, curr):
    if (n == 0):
        return curr
    elif (n < 0):
        return sys.maxint;
    else:
        best = sys.maxint
        if len(denoms) > 0:
            i = 0
            while (i * denoms[0] <= n):
                best = min(best, getMinChange(n - i*denoms[0], denoms[1:], curr+i))
                i += 1
        return best
