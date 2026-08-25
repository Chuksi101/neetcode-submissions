# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        stack = [(p,q)]
        while stack:
        # if p.val == q.val:
        #     left = self.isSameTree(p.left, q.left)
        #     right = self.isSameTree(p.right, q.right)
        #     return left and right
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