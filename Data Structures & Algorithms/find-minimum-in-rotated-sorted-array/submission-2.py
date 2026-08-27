class Solution:
    def findMin(self, nums: List[int]) -> int:
        if nums[0] <= nums[-1]:
            return nums[0]
        
        l, r = 0, len(nums) - 1
        lowest = nums[0]

        while l <= r:
            if nums[l] < nums[r]:
                lowest = min(lowest, nums[l])

            m = (l + r) // 2
            lowest = min(lowest, nums[m])

            if nums[m] >= nums[l]:
                l = m + 1
            elif nums[m] < nums[l]:
                r = m - 1
        
        return lowest
