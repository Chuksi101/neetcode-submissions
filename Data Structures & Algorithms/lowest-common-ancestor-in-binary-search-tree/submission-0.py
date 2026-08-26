# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        '''
        - Check if root == p || root == q; return root
        - if not, 
            left = lca(root.left, p, q)
            right = lca(root.right, p, q)
        - if left and right, return root
        - if left, return left; else return right
        '''
        if root == q or root == p:
            return root
        if root:
            left = self.lowestCommonAncestor(root.left, p, q)
            right = self.lowestCommonAncestor(root.right, p, q)
            if left and right:
                return root
            elif left:
                return left
            else:
                return right