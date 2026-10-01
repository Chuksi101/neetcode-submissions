# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        '''
        - Use dfs(node, height)
            - if not node, return (True, 0) {balanced, height}
            - run dfs on left and right with +1 to height
            - if left is balanced and right is balanced and height of left - right <= 1
            - return (balanced, max(height of left and right))

        - return dfs[0]
        '''

        def dfs(node, height):
            if not node:
                return (True, height)

            left = dfs(node.left, 1 + height)
            right = dfs(node.right, 1 + height)

            balanced = left[0] and right[0] and abs(left[1]-right[1]) <= 1

            return (balanced, max(left[1], right[1]))

        return dfs(root,0)[0]