# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def insertionSort(self, pairs: List[Pair]) -> List[List[Pair]]:
        arlen = len(pairs)
        if arlen == 0:
            return []
        final = []
        final.append(pairs[:])
        for i in range(1, arlen):
            
            j = i - 1
            while (j >= 0 and pairs[j].key > pairs[j+1].key):
                
                tmp = pairs[j]
                pairs[j] = pairs[j+1]
                pairs[j+1] = tmp
                j -= 1
            final.append(pairs[:])
        return final
        