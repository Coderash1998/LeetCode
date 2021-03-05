"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        v=[]
        def traverse(root):
            if root==None:
                return None
            if root.children !=None:
                for i in root.children:
                    traverse(i)
            v.append(root.val)
        traverse(root)
        return v