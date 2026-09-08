class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        '''
        initialize pointers: r,l,seen (dict),res
        Loop through all the elements e in s (for r in range(len(s))):
            - update the count of e in the seen dict
            - while r-l+1 - maxSeen (max of seen.values()) > k:
                - reduce count of l in the seen dict
                - l += 1
            - res = max(res, r-l+1)

        '''
        l = r = res = 0
        seen = {}

        for r in range(len(s)):
            seen[s[r]] = seen.get(s[r], 0) + 1
            while (r-l+1) - max(seen.values()) > k:
                print(s[l])
                seen[s[l]] -= 1
                l += 1
            res = max(res, (r-l)+1)
        
        return res
