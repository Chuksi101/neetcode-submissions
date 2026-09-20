class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        adjMap = {i: [] for i in range(numCourses)}
        for crs,pre in prerequisites:
            adjMap[crs].append(pre)
        visited = set()

        def dfs(c):
            if c in visited:
                return False
            if adjMap[c] == []:
                return True

            visited.add(c)
            for p in adjMap[c]:
                if not dfs(p):
                    return False

            visited.remove(c)
            adjMap[c] = []
            return True

        for i in range(numCourses):
            if not dfs(i):
                return False
        return True