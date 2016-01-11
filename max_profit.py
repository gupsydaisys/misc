#####################################################################################
# Design an algorithm that determines the maximum profit that could have been made
# by buying and then selling a single share over a given day range, subjec to the
# constraint that the buy and the sell ahve to take place at the start of the day.
#####################################################################################

# a = [0, -2, 2, 1, -3, 5, 0]


# Runs in o(n^2)
def getMaxProfit(arr):
    l = [(i, item) for i, item in enumerate(arr)]
    lSort = sorted(l, key=lambda x: x[-1])
    m = 0
    for i in range(len(lSort)):
        j = len(lSort) - 1
        while (i != j):
            diff = lSort[j][1] - lSort[i][1]
            if (lSort[i][0] < lSort[j][0]) and (diff > m):
                m = diff
            j -= 1
    return m



import sys
# Runs in o(n) uses o(n) extra space
# Assume you will not buy and sell if your profit is non-positive
def getMaxProfit2(arr):
    maxs = [l[-1]]
    for i in reversed(range(len(arr) - 1)):
        if (maxs[0] > arr[i]):
            maxs.insert(0, maxs[0])
        else:
            maxs.insert(0, arr[i])
    m = -sys.maxint - 1
    for i in range(len(arr)):
        diff = maxs[i] - arr[i] 
        m = diff if diff > m else m
    return m