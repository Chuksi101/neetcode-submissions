class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l1 = len(s1)
        l2 = len(s2)
        if l1 > l2:
            return Counter(s2) == Counter(s1)
            
        s1c = Counter(s1)
        s2c = Counter(s2[:l1])

        for r in range(l1,l2+1):
            if s1c == s2c:
                return True
            # Remove leftmost letter
            s2c[s2[r-l1]] -= 1
            if s2c[s2[r-l1]] == 0:
                del s2c[s2[r-l1]]

            # Add new letter
            if r < l2:
                s2c[s2[r]] = s2c.get(s2[r], 0) + 1
        return False