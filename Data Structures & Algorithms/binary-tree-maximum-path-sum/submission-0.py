# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = float('-inf')

        def dfs(node):
            nonlocal res
            if not node:
                return 0

            leftsum = dfs(node.left)
            rightsum = dfs(node.right)

            bestleft = max(leftsum,0)
            bestright = max(rightsum, 0)

            res = max(res, node.val + bestleft + bestright)

            return node.val + max(bestleft, bestright)

        dfs(root)
        return res