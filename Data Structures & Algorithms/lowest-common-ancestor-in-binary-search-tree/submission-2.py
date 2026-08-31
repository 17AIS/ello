# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if p.val > q.val:
            big = p
            small = q
        else:
            big = q
            small = p
        if small.val <= root.val and root.val <= big.val:
            return root
        

        stack = [root]

        while stack:
            curr = stack.pop()
            
            print(curr.val)
            print(small.val <= curr.val, curr.val <= big.val)
            print()
            if small.val <= curr.val and curr.val <= big.val:
                return curr
            
            if curr.right:
                stack.append(curr.right)
            if curr.left:
                stack.append(curr.left)
        
        return root