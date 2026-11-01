class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        lena = len(s)
        if lena <= 1:
            return lena
        l,r = 0, 1
        curset = set()
        curset.add(s[l])
        curmax = 1
        while r < lena:
            while s[r] in curset:
                curset.remove(s[l])
                l += 1
            curset.add(s[r])
            curmax = max(r - l + 1, curmax)
            r += 1
            
        return curmax