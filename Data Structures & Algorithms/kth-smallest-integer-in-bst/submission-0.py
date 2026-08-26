# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        '''
        - in-order traversal stored to list
        - go to k-1 index
        '''
        return self.inorder_recursive(root)[k-1]
        

    def inorder_recursive(self, root):
        result = []
        
        def traverse(node):
            if not node:
                return
            
            traverse(node.left)       # 1. Traverse Left
            result.append(node.val)   # 2. Visit Node
            traverse(node.right)      # 3. Traverse Right

        traverse(root)
        return result
