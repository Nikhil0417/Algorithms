# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if(root != None):
            l = self.maxDepth(root.left)
            r = self.maxDepth(root.right)
            if(l>r):
                return l+1
            else:
                return r+1
        else:
            return 0
