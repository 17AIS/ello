# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root or (not root.left and not root.right):
            return root

        def rec(curr):
            if curr.right:
                rec(curr.right)
            if curr.left:
                rec(curr.left)
            
            temp = curr.right
            curr.right = curr.left
            curr.left = temp

        
        rec(root)
        return root