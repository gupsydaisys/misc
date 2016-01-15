# Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

# For example, given n = 3, a solution set is:

# "((()))", "(()())", "(())()", "()(())", "()()()"

# n = 1 -> ()
# n = 2 -> ()() or (())


# (
# ) BAD
# ()
# ((
# ())
# ()(
# # Rule can't close parenthesis without warning

   
def helper(curr, numLefts, numRights):
    if numLefts > numRights or numLefts < 0 or numRights < 0:
        return []
    elif numLefts == numRights == 0:
        return [curr]
    else:
        h0 = helper(curr + "(", numLefts-1, numRights)
        h1 = helper(curr + ")", numLefts, numRights-1)
        return h0 + h1

def getCombos(n):
        return helper("", n, n)

assert getCombos(1) == ['()'] 
assert getCombos(2) == ['(())', '()()'] 
assert getCombos(3) == ['((()))', '(()())', '(())()', '()(())', '()()()'] 
