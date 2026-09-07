class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l1 = len(s1)
        l2 = len(s2)
        if l1 >= l2:
            return Counter(s2) == Counter(s1)
            
        s1c = Counter(s1)
        for i in range((l2-l1)+1):
            s2c = Counter(s2[i:i+l1])
            if s1c == s2c:
                return True
        return False