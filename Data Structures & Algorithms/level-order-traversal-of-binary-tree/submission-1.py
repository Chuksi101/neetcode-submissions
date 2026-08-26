# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        res = []
        q = deque()
        q.append(root)
        while q:
            level = []
            for i in range(len(q)):
                curr = q.popleft()
                if curr:
                    q.append(curr.left)
                    q.append(curr.right)
                    level.append(curr.val)
            if level:
                res.append(level)

        return res