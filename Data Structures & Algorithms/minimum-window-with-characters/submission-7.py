class Solution:
    def minWindow(self, s: str, t: str) -> str:
        ts = Counter(t)
        required = len(ts)
        m = None
        i,j = 0,0
        ss = Counter()
        formed = 0

        while j < len(s):
            ss[s[j]] += 1
            if s[j] in ts and ss[s[j]] == ts[s[j]]:
                formed += 1
            j += 1

            while formed == required:
                curr = s[i:j]
                if m is None or len(curr) < len(m):
                    m = curr
                ss[s[i]] -= 1

                if s[i] in ts and ss[s[i]] < ts[s[i]]:
                    formed -= 1

                i += 1

        return "" if m is None else m