class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        cur = res = 0

        for i in range(len(nums)):
            if nums[i] == res:
                cur += 1
            elif cur == 0:
                res = nums[i]
                cur = 1
            else:
                cur -= 1
        
        return res