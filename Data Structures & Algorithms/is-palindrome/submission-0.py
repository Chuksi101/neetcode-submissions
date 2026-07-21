class Solution:
    def isPalindrome(self, s: str) -> bool:
        modifiedString = "".join(char.lower() for char in s if char.isalnum())
        l = r = len(modifiedString)//2
        if len(modifiedString) % 2 == 0:
            l -= 1
        while l >= 0 and r < len(modifiedString):
            if modifiedString[l] != modifiedString[r]:
                return False
            l -= 1
            r += 1
        return True
