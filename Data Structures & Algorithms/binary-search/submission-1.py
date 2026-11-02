class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 0:
            return -1
        r = len(nums) - 1
        l = 0
        if nums[r] == target:
            return r
        if nums[l] == target:
            return l
        mid = ((r - l) // 2) + l 
        print(mid)

        while mid != l:
            if nums[mid] == target:
                return mid
            if nums[mid] < target:
                l = mid
            else:
                r = mid
            mid = ((r-l) // 2) + l
            print(mid)
        return -1



        