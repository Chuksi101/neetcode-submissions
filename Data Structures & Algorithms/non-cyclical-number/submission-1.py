class Solution:
    def isHappy(self, n: int) -> bool:
        curr = n
        seen = set()
        while True:
            total = 0
            for i in str(curr):
                total += (int(i) ** 2)
            if total in seen:
                return False
            elif total == 1:
                return True
            else:
                seen.add(total)
                curr = total
