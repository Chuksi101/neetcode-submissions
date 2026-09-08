class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        '''
        initialize pointers: r,l,seen (dict),maxSeen,res
        Loop through all the elements e in s (for r in range(len(s))):
            - update the count of e in the seen dict
            - update maxSeen if the count is greater than current r 
            - while r-l+1 - maxSeen > k:
                - reduce count of l in the seen dict
                - l += 1
            - res = max(res, r-l+1)

        '''
        l = r = res = maxSeen = 0
        seen = {}

        for r in range(len(s)):
            seen[s[r]] = seen.get(s[r], 0) + 1
            maxSeen = max(maxSeen, seen[s[r]])
            while (r-l+1) - maxSeen > k:
                seen[s[l]] -= 1
                l += 1
            res = max(res, (r-l)+1)
        
        return res
