# Given a digit string, return all possible letter combinations that the number 
# could represent. (Check out your cellphone to see the mappings) 
# Input:Digit string "23", Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].

d = {}
d["2"] = ["a", "b", "c"]
d["3"] = ["d", "e", "f"]
d["4"] = ["g", "h", "i"]
d["5"] = ["j", "k", "l"]
d["6"] = ["m", "n", "o"]
d["7"] = ["p", "q", "r", "s"]
d["8"] = ["t", "u", "v"]
d["9"] = ["w", "x", "y", "z"]

# Assume only valid ints are part of str
def getAllCombos(str, lst):
    if len(str) == 0:
        return lst
    out = []
    for e in d[str[0]]:
        copy = [item + e for item in lst]   
        out = out + getAllCombos(str[1:], copy)
    return out

a = ['a', 'b', 'c'] 
b = ['ad', 'ae', 'af', 'bd', 'be', 'bf', 'cd', 'ce', 'cf'] 
c = ['adg', 'adh', 'adi', 'aeg', 'aeh', 'aei', 'afg', 'afh', 'afi', 'bdg', 'bdh', 'bdi', 'beg', 'beh', 'bei', 'bfg', 'bfh', 'bfi', 'cdg', 'cdh', 'cdi', 'ceg', 'ceh', 'cei', 'cfg', 'cfh', 'cfi'] 

assert getAllCombos("", [""]) == ['']
assert getAllCombos("2", [""]) == a
assert getAllCombos("23", [""]) == b
assert getAllCombos("234", [""]) == c

# Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.
# For example, if n = 4 and k = 2, a solution is:
# [
#   [2,4],
#   [3,4],
#   [2,3],
#   [1,2],
#   [1,3],
#   [1,4],
# ]

def helper(lst, k):
    if k == 0:
        return []
    else:
        out = []
        for i, e in enumerate(lst):
            if len(lst[i+1:]) >= k - 1:
                newLst = helper(lst[i+1:], k - 1)
                if newLst == []:
                    out = out + [[e]]
                else:
                    newLst = [[e] + newItem for newItem in newLst]
                    out = out + newLst
        return out
                
# Assume n > 0 and n >= k
def getKLengthCombos(n, k):
    lst = [i for i in range(1, n+1)]
    return helper(lst, k)

assert getKLengthCombos(1, 1) == [[1]]
assert getKLengthCombos(4, 0) == []
assert getKLengthCombos(4, 1) == [[1], [2], [3], [4]]
assert getKLengthCombos(4, 2) == [[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]]
assert getKLengthCombos(4, 3) == [[1, 2, 3], [1, 2, 4], [1, 3, 4], [2, 3, 4]] 

# Find all possible combinations of k numbers that add up to a number n, given that only numbers from 1 to 9 can be used and each combination should be a unique set of numbers.
# Ensure that numbers within the set are sorted in ascending order.
# Example 1: Input: k = 3, n = 7 Output: [[1,2,4]]
# Example 2: Input: k = 3, n = 9 Output: [[1,2,6], [1,3,5], [2,3,4]]
# assume k > 0
# k = 1, n = 7 -------> [[7]]
# k = 2, n = 7  -------> 16 25 34

def helper(k, n, lst):
    if k == 1:
        if n in lst:
            return [[n]]
        else:
            return [[]]
    else:
        lsts = []
        for i, e in enumerate(lst):
            curr = helper(k-1, n-e, lst[i+1:])
            if curr and curr[0]:
                lsts = lsts + [[e] + c for c in curr]
        return lsts                

def getAllKSizeSums(k, n):
    return helper(k, n, [i for i in range(1, 10)])
    
assert getAllKSizeSums(1, 7) == [[7]]
assert getAllKSizeSums(2, 7) == [[1,6], [2, 5], [3, 4]]
assert getAllKSizeSums(3, 7) == [[1,2,4]]
assert getAllKSizeSums(3, 9) == [[1,2,6], [1,3,5], [2,3,4]]

# Given a collection of candidate numbers (C) and a target number (T), find all unique combinations in C where the candidate numbers sums to T. Each number in C may only be used ONCE in the combination.

# Note:
# 1) All numbers (including target) will be positive integers.
# 2) Elements in a combination (a1, a2, … , ak) must be in non-descending order. (ie, a1 ≤ a2 ≤ … ≤ ak).
# 3) The solution set must not contain duplicate combinations.

# 1, 2, 4, 5    10
# 1 4 5

def func(C, t):
    if sum(C) < t or not [t < e for e in C]:
        return [[]]
    else:
        lsts = []
        for i, e in enumerate(C):
            if t - e == 0:
                lsts = lsts + [[e]]
            else:
                c = func(C[i+1:], t - e)
                if c and c[0]:
                    lsts = lsts + [[e] + item for item in c]
        return lsts
    
assert func([1, 2, 3, 4, 5, 10], 10) == [[1, 2, 3, 4], [1, 4, 5], [2, 3, 5], [10]]

# Given a collection of candidate numbers (C) and a target number (T), find all unique combinations in C where the candidate numbers sums to T. Each number in C may only be used ONCE in the combination.

# Note:
# 1) All numbers (including target) will be positive integers.
# 2) Elements in a combination (a1, a2, … , ak) must be in non-descending order. (ie, a1 ≤ a2 ≤ … ≤ ak).
# 3) The solution set must not contain duplicate combinations.

# 1, 2, 4, 5    10
# 1 4 5

def func(C, t):
    if t < 0:
        return [[]]
    else:
        lsts = []
        for i, e in enumerate(C):
            if t - e == 0:
                lsts = lsts + [[e]]
            else:
                c = func(C[i:], t - e)
                if c and c[0]:
                    lsts = lsts + [[e] + item for item in c]
        return lsts
    
print func([2,3,6,7], 7) 