# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        def traverse(root):
            if not root:
                return None
            s,l=[root],[]
            while(s):
                n=s.pop()
                if not n: continue
                s.append(n.left)
                s.append(n.right)
                if not (n.left or n.right):
                    l.append(n.val)
            return l
        return traverse(root1)==traverse(root2)