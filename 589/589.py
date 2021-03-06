"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        v=[]
        def traverse(root):
            if root==None:
                return None
            if root!=None:
                v.append(root.val)
                for i in root.children:
                    traverse(i)
        traverse(root)
        return v
        