class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        while n not in seen:
            seen.add(n)
            total = 0
            for i in str(n):
                total += (int(i) ** 2)
            if total == 1:
                return True
            else:
                n = total
        return False
