class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        curmax = nums[0]
        cur = nums[0]
        for n in nums[1:]:
            print(cur)
            cur = max(cur, 0)
            cur += n
            if cur >= curmax:
                curmax = cur
        return curmax
        