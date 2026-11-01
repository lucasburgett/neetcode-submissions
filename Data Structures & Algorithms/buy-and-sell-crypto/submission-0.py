class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lena = len(prices)
        if lena == 0:
            return 0
        l = 0
        r = 1
        allmax = 0
        curmax = 0

        while r < lena:
            if prices[r] > prices[l]:
                curmax = prices[r] - prices[l]
                allmax = max(allmax, curmax)
                r += 1
            else:
                l = r
                r += 1
        return allmax



        