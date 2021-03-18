# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: TreeNode) -> int:
        self.s=0
        def dfs(node, n):
            if not node: 
                return None
            n=n*2+node.val
            if not node.left and not node.right:
                self.s+=n
                return
            dfs(node.left,n)
            dfs(node.right,n)
        dfs(root,0)
        return self.s