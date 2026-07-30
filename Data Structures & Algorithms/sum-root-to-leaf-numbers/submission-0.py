# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        if not root.right and not root.left:
            return root.val

        
        stack = [[root, str(root.val)]]
        total = 0
        while stack:
            curr, val = stack.pop()

            if curr.left == None and curr.right == None:
                print(total)
                total += int(val)

            if curr.left:
                temp = val + str(curr.left.val)
                stack.append([curr.left, temp])
            
            if curr.right:
                temp = val + str(curr.right.val)
                stack.append([curr.right, temp])

        return total