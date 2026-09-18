# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        '''
        - Build a dictionary of inorder indicies (use enumerate) 
        - initialize a preorder index
        - dfs
            - l > r: return
            - get current val at index (Use preorder list)
            - increment index
            - use the recursive solution of breaking into left and right subtree but mid is the inorder index of currentVal (use dictionary)
        '''
        store = {val: pos for pos, val in enumerate(inorder)}
        preorderIndex = 0

        def dfs(l, r):
            nonlocal preorderIndex

            if l > r:
                return

            currentVal = preorder[preorderIndex]
            preorderIndex += 1
            node = TreeNode(currentVal)
            mid = store[currentVal]

            node.left = dfs(l, mid-1)
            node.right = dfs(mid+1, r)
            return node

        return dfs(0, len(preorder)-1)
