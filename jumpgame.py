# Given an array of non-negative integers, you are initially positioned at the first index 
# of the array. Each element in the array represents your maximum jump length at that position. 
# Determine if you are able to reach the last index. For example: A = [2,3,1,1,4], return true.
#  A = [3,2,1,0,4], return false.


def helper(usedIndices, arr, currIndex):
    # Goldylox
    if currIndex == len(arr)-1:
        return True
    # Index out of bounds
    if currIndex > len(arr)-1 or currIndex < 0:
        return False
    # Cycle check
    if currIndex in usedIndices:
        return False
    else:
        usedIndices.add(currIndex)
    return helper(usedIndices, arr, currIndex + arr[currIndex]) or helper(usedIndices, arr, currIndex - arr[currIndex])


def getGetLastIndex(arr):
        return helper(set(), arr, 0)
    
assert getGetLastIndex([2,3,1,1,4]) == True
assert getGetLastIndex([3,2,1,0,4]) == False