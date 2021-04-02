"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if root==None:
            return 0
        else:
            d=0
            for i in (root.children):
                d= max(d,self.maxDepth(i))
            return 1+d