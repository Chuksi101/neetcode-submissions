# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    '''
    - use a list to serialize (convert to list and then string) {2n+1, 2n+2 for children}
        - Do we want to encode null children for the root node (in case of a single node)
    - use index to deserialize
    '''
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        res = ""
        if not root:
            return ""
        q = deque()
        q.append(root)

        while q:
            curr = q.popleft()
            if curr:
                res = res + str(curr.val) + '|'
                q.append(curr.left)
                q.append(curr.right)
            else:
                res += 'N|'

        print(res)
        return res



        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if data == "":
            return None

        dataList = data.split("|")[:-1]
        root = TreeNode(int(dataList[0]))
        q = deque()
        q.append(root)
        i = 1

        while q:
            parent = q.popleft()

            token = dataList[i]
            if token != 'N':
                lc = TreeNode(token)
                parent.left = lc
                q.append(lc)
            i += 1
            
            token = dataList[i]
            if token != 'N':
                rc = TreeNode(token)
                parent.right = rc
                q.append(rc)
            i += 1
        
        return root
        

