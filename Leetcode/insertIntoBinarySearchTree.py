# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def insertIntoBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        if root is None:
            root = TreeNode(val)
            root.left = None
            root.right = None
            return root
        else:
            if(val<root.val):
                root.left = self.insertIntoBST(root.left,val)
            if(val>root.val):
                root.right = self.insertIntoBST(root.right,val)
            return root