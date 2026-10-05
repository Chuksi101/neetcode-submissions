# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res = 0
        def checkNode(base, node):
            nonlocal res
            if not node:
                return

            if node.val >= base:
                res += 1
                
            newBase = max(base, node.val)
            checkNode(newBase, node.left)
            checkNode(newBase, node.right)

        checkNode(float('-inf'), root)
        return res
