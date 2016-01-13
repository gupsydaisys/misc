#####################################################################################
# Given two strings s (search string) and t (text) find all occurences of s in t
#####################################################################################

def strSearch(s, t):
    if len(t) > len(s):
        return 0
    return sum([1 if s[i:i+len(t)] == t else 0 for i in range(len(s) - len(t) + 1)])

def strSearch2(s, t):
    if len(t) > len(s):
        return 0
    lst = [i for i in range(len(s) - len(t) + 1)]
    for j in range(len(t)):
        temp = []
        for i in lst:
            if s[j+i] == t[j]:
                temp.append(i)
        lst = temp
        if len(lst) == 0:
            return 0
    return len(lst)

#####################################################################################
# Is one string a rotation of another?
#####################################################################################
def isRot(s, t):
    #car #arc
    if len(s) != len(t):
        return False
    for startIndex in range(len(t)):
        concat = t[startIndex:] + t[:startIndex]
        if concat == s:
            return True
    return False

def isRot2(s, t):
    #car #arc
    return True if strSearch2(t + t, s) > 0 else False
