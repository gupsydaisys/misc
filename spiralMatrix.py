############################################################
# Write a function to print out a matrix in spiral form.
# You'll read input from STDIN and print output to STDOUT.
# First line is rows, columns. Rest are values in matrix.
# Output all values in spiral order.
############################################################
import sys

out = []
# runtime is O(n*m*max(n,m))
def printOutSides(mat):
    # print mat
    # BASE CASE
    if len(mat) == 0 or len(mat[0]) == 0:
        return   
    if len(mat) == 1:
        for e in mat[0]:
            out.append(e)
        return
    if len(mat[0]) == 1:
        for e in mat:
            out.append(e[0])
        return
    for i in range(len(mat[0])):
        out.append(mat[0][i])
    for i in range(1, len(mat)): 
        out.append(mat[i][len(mat[0]) - 1])
    for i in reversed(range(len(mat[0]) - 1)):
        out.append(mat[len(mat) - 1][i])
    for i in reversed(range(1, len(mat) - 1)):
        out.append(mat[i][0])
    newMat = [[mat[i][j] for j in range(1, len(mat[0]) - 1)] for i in range(1, len(mat) - 1)]
    printOutSides(newMat)

def printOutSidesMain():
    print sys.stdin.readline()
    matrix = [[int(x.strip()) for x in line.split(',')] for line in sys.stdin]
    printOutSides(matrix)
    str0 = ""
    for elem in out:
        str0 += str(elem) + ","
    print str0[:len(str0)-1]

# O(nm)
def printOutSides2(mat):
    for offset in range(0,int(max(len(mat[0]), len(mat))/2.0)):
        for j in range(offset, len(mat[0]) - offset):
            out.append(mat[offset][j])
        for i in range(1 + offset, len(mat) - offset):
            out.append(mat[i][len(mat[0]) - 1 - offset])
        if len(mat) - offset*2 != 1:
            for j in reversed(range(offset, len(mat[0]) - 1 - offset)):
                out.append(mat[len(mat) - 1 - offset][j])
        if len(mat[0]) - offset*2 != 1:
            for i in reversed(range(1 + offset, len(mat) - 1 - offset)):
                out.append(mat[i][offset])

m0 = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
m1 = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
m2 = [[1, 2, 3], [5, 6, 7], [9, 10, 11], [13, 14, 15]]
m3 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

m = [m0, m1, m2, m3]
for e in m:
    out = []
    printOutSides(e)
    str0 = ""
    for elem in out:
        str0 += str(elem) + ","
    print str0[:len(str0)-1]
