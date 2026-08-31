# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        stack = [[root, -1000000001, 1000000001]]
        vals = set()

        while stack:
            curr, small, big = stack.pop()
            if curr.val in vals:
                return False
            vals.add(curr.val)

            if curr.right:
                if curr.right.val > big or curr.right.val <= curr.val:
                    return False
                stack.append([curr.right, curr.val, big])
            
            if curr.left:
                if curr.left.val < small or curr.left.val >= curr.val:
                    return False
                stack.append([curr.left, small, curr.val])

        return True







