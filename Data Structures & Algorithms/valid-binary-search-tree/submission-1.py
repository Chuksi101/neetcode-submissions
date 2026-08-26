# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        stack = [(root, [float('-inf'), float('inf')])]

        while stack:
            node, interval = stack.pop()
            if node.val <= interval[0] or node.val >= interval[1]:
                return False
            if node.left:
                stack.append((node.left, [interval[0], node.val]))
            if node.right:
                stack.append((node.right,[node.val, interval[1]]))
        
        return True
    