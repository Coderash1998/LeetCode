# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        l = []
        def inorder(root):
            if root:
                inorder(root.left)
                l.append(root.val)
                inorder(root.right)
        inorder(root)
        t = TreeNode(l[0])
        n = t
        for i in range(1, len(l)):
            n.right = TreeNode(l[i])
            n = n.right
        return t