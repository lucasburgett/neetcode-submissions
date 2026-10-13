class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        words = {}
        final = []
        for s in strs:
            alpha = {}
            for l in s:
                if l not in alpha:
                    alpha[l] = 0
                alpha[l] += 1
            sort = tuple(sorted(alpha.items()))
            if sort not in words:
                words[sort] = []
            words[sort].append(s)
        return list(words.values())
            
            

        