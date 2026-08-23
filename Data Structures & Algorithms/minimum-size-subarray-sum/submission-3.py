class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l, r = 0, 0
        result = len(nums) + 1

        windowSum = 0
        for r in range(len(nums)):
            windowSum += nums[r]

            while windowSum - nums[l] >= target:
                windowSum -= nums[l]
                l += 1
            
            if windowSum >= target:
                result = min(result, r - l + 1)
        
        if result == len(nums) + 1:
            return 0
        return result