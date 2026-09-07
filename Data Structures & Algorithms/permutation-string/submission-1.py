class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) >= len(s2):
            return Counter(s2) == Counter(s1)
            
        s1c = Counter(s1)
        l1 = len(s1)
        for i in range((len(s2)-l1)+1):
            print(s2[i:i+l1])
            s2c = Counter(s2[i:i+l1])
            if s1c == s2c:
                return True
        return False