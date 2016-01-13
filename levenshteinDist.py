import sys

#####################################################################################
# Get the levenshtein distance between two strings which is the minimum number
# of insertions, deletions, and substitutions to go from STR0 to STR1.
#####################################################################################

# O(3^n)
def getLDist(str0, str1):
    #base case
    if str0 == "" and str1 == "":
        return 0
    #all okay
    if (len(str1) > 0) and (len(str0) > 0) and (str0[0] == str1[0]):
        return getLDist(str0[1:], str1[1:])
    bestDist = sys.maxint
    #insert
    if (len(str0) > 0):
        bestDist = min(bestDist, getLDist(str0[1:], str1))
    #delete
    if (len(str1) > 0):
        bestDist = min(bestDist, getLDist(str0, str1[1:]))
    #substitute
    if (len(str1) > 0) and (len(str0) > 0):
        bestDist = min(bestDist, getLDist(str0[1:], str1[1:]))
    return 1 + bestDist

# O(len(str0)*len(str1))
def getLDist2(str0, str1):
    m = [[0 for i in range(len(str1) + 1)] for i in range(len(str0) + 1)]
    m[0][0] = 0
    for i in range(1, len(str0) + 1):
        m[i][0] = 1
    for j in range(1, len(str1) + 1):
        m[0][j] = 1
    for i in range(1, len(str0) + 1):
        for j in range(1, len(str1) + 1):
            if str0[i-1] == str1[j-1]:
                m[i][j] = m[i-1][j-1]
            else:
                m[i][j] = 1 + min(m[i][j-1], m[i-1][j], m[i-1][j-1])
    return m[len(str1)][len(str0)]

    