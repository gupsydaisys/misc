# Given an array of integers, every element appears three times except for one. 
# Find that single one.

# Take each number and convert to binary
# Sum each digit across all array indices and mod 3 to get that digit in the answer
def findSingleElem(arr):
    dict = {}
    for e in arr:
        while e != 0:
            i = 0
            while (2**i <= e):
                i += 1
            i = i - 1
            if i in dict:
                dict[i] = dict[i] + 1
            else:
                dict[i] = 1   
            e = e - 2**i
    i = 0
    n = 0
    for i in dict:
        n += (dict[i] % 3)*(2**i)
    return n


assert findSingleElem([1]) == 1
assert findSingleElem([34]) == 34
assert findSingleElem([34, 2, 2, 2]) == 34
assert findSingleElem([2, 2, 34, 2]) == 34
assert findSingleElem([2, 2, 2, 34]) == 34
assert findSingleElem([2, 2, 7, 34, 2, 7, 7]) == 34