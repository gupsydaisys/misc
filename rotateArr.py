#####################################################################################################################
# Rotate an array of n elements to the right by k steps. For example, 
# with n = 7 and k = 3, the array [1,2,3,4,5,6,7] is rotated to 
# [5,6,7,1,2,3,4]. How many different ways do you know to solve this problem?
####################################################################################################################


# n = 7, k = 4
# 1 2 3 4 5 6 7 -> 4 5 6 7 1 2 3

# n = 7, k = 2
# 1 2 3 4 5 6 7 -> 6 7 1 2 3 4 5

# Assume n > 0 and n >= k >= 0 and both are ints.
def rotateArray(n, k):
    lst = [i for i in range(n-k+1, n+1)]
    for i in range(1, n-k+1):
        lst.append(i)
    print lst

def rotateArray(n, k):
    print [i-k if i > k else n-k+i for i in range(1, n+1)]

rotateArray(7, 4)
rotateArray(7, 2)
rotateArray(7, 0)
rotateArray(1, 0)
rotateArray(7, 7)
rotateArray(7, 8)

# Rotate a given array
def rotateArray(lst, k):
    n = len(lst)
    print [lst[i-k] if i >= k else lst[n-k+i] for i in range(0, n)]
