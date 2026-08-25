# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root:
            return False
        
        stack = [(root, subRoot)]
        while stack:
            r,s = stack.pop()
            if self.isSameTree(r, s):
                return True
            if r:
                stack.append((r.left, subRoot))
                stack.append((r.right, subRoot))
        return False


    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        stack = [(p,q)]
        while stack:
            left,right = stack.pop()
            if not left and not right:
                continue
            elif not left or not right:
                return False
            else:
                if left.val == right.val:
                    stack.append((left.left, right.left))
                    stack.append((left.right, right.right))
                else:
                    return False
        return True