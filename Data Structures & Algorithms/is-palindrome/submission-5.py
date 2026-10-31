class Solution:
    def isPalindrome(self, s: str) -> bool:
        slen = len(s)
        if slen <= 1:
            return True
        r = slen - 1
        l = 0
        while l <= r:
            while not s[l].isalnum() and l < r:
                l += 1
            while not s[r].isalnum() and l < r:
                r -= 1
            if s[r].lower() != s[l].lower():
                return False
            l += 1
            r -= 1

        return True