class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxw = 0
        l = 0
        r = 0
        temp = set()
        while r < len(s):
            if s[r] not in temp:
                temp.add(s[r])
                r += 1
                maxw = max(r-l, maxw)
            else:
                temp.remove(s[l])
                l += 1
        return maxw