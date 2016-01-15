# Reverse a singly linked list.

class Node:
  def __init__(self,val,nxt):
    self.val = val
    self.nxt = nxt

def prnt(n):
  if(n is not None):
    nxt = n.nxt
    print n.val
    prnt(nxt)
    
def reverse(L):
    if not L:
        return L
    curr = L
    next = L.nxt
    first = True
    while next:
        temp = next.nxt
        next.nxt = curr
        if first:
            curr.nxt = None
            first = False
        curr = next
        next = temp
    return curr

prnt(reverse(Node(1, Node(2, Node(3, None)))))
prnt(reverse(None))
prnt(reverse(Node(11, None)))

