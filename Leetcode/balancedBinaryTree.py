# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isBalanced(self, root: 'TreeNode') -> 'bool':
        if root is None:
            return True
        else:
            return abs(self.height(root.left)-self.height(root.right))<2 and self.isBalanced(root.left) and self.isBalanced(root.right)
    def height(self, root):
        if root is None:
            return 0
        else:
            l = self.height(root.left)
            r = self.height(root.right)
            if l>r:
                return l+1
            else:
                return r+1
