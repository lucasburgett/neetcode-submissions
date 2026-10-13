# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:
        arlen = len(pairs)
        if arlen <= 1:
            return pairs
        mid = arlen // 2
        first = pairs[mid:]

        last = pairs[:mid]

        first = self.mergeSort(first)
        last = self.mergeSort(last)


        lenl = len(first)
        lenj = len(last)
        i, j = 0, 0
        final = []
        while i < lenl and j < lenj:
            if first[i].key < last[j].key:
                final.append(first[i])
                i += 1
            else:
                final.append(last[j])
                j += 1
        if i != lenl:
            while i < lenl:
                final.append(first[i])
                i += 1
        if j != lenj:
            while j < lenj:
                final.append(last[j])
                j += 1
        return final
        
            
