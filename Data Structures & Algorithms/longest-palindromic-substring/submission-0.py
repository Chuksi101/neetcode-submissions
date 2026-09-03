class Solution:
    def longestPalindrome(self, s: str) -> str:
        initialIndex = 0
        plen = 0

        for i in range(len(s)):
            l = r = i
            #Odd Loop
            while l >= 0 and r < len(s) and s[l] == s[r]:
                # Add section on checking vs current length of palindrome
                if (r-l+1) > plen:
                    initialIndex = l
                    plen = r-l+1
                l -= 1
                r += 1
            
            # Even Loop
            l, r = i, i+ 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                # Add section on checking vs current length of palindrome
                if (r-l+1) > plen:
                    initialIndex = l
                    plen = r-l+1
                l -= 1
                r += 1

        return s[initialIndex:initialIndex+plen]