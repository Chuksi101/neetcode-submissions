class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        '''
        - We want to use binary search here

        - start with mid (max + 1 // 2) value and check if that eating rate would be viable
            - if yes, use that as the new max. If not, use it as the new min (To replace 1) and we want to go mid + 1
        '''

        t = max(piles)
        l = 1

        while l < t:
            k = (t + l) // 2
            total = 0
            for p in piles:
                total += math.ceil(p/k)
            
            if total > h:
                l = k + 1
            else:
                t = k
        return l
