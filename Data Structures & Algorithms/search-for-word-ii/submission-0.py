class Trie:
    def __init__(self):
        self.children = {}
        self.isEnd = False
        

    def addWord(self, word: str) -> None:
        cur = self
        for c in word:
            if c not in cur.children:
                cur.children[c] = Trie()
            cur = cur.children[c]
        cur.isEnd = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        '''
        - Build a Trie class (Can copy from the other)
            - init
            - add words method
        in findwords class
        - initialize a root Trie
        - initialize a visited set
        - initialize a result set
        - for every word in words
            - Add word to root Trie

        - We're using dfs to search
        - Define a dfs method (row, col, TrieNode {}, word {current path})
            - Boundary check, check if curr node in Trie, check if cell in visited

            - add cell to visited set
            - go to Trie node {like curr[board[r][c]]}
            - append new letter to word
                - if word append to result
            - run dfs in every direction
            - remove cell from visited

        - for loop for each row and column cell
            - dfs

        - return list(res)
        '''
        root = Trie()
        visited = set()
        result = set()
        
        for word in words:
            root.addWord(word)

        def dfs(row, col, node, wordPath):
            curr = node
            if row > len(board)-1 or col > len(board[0])-1 or row < 0 or col < 0 or (row,col) in visited or board[row][col] not in curr.children:
                return

            visited.add((row,col))
            letter = board[row][col]
            curr = curr.children[letter]
            wordPath += letter
            if curr.isEnd:
                result.add(wordPath)
                
            dfs(row+1, col, curr, wordPath)
            dfs(row, col+1, curr, wordPath)
            dfs(row-1, col, curr, wordPath)
            dfs(row, col-1, curr, wordPath)
            visited.remove((row,col))

        for i in range(len(board[0])):
            for j in range(len(board)):
                dfs(j, i, root, '')

        return list(result)
        