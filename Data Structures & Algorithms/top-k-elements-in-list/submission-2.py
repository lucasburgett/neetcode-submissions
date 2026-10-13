class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numd = {}
        for num in nums:
            if num not in numd:
                numd[num] = 0
            numd[num] += 1
        sortedl = sorted(list(numd.items()), reverse = True, key=lambda x: x[1])
        final = []
        for i in range(k):
            final.append(sortedl[i][0])
        return final

        