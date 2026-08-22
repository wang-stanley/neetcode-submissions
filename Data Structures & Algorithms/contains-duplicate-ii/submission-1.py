class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        windowSet = set()

        l, r = 0, 0

        while r < len(nums):
            if nums[r] in windowSet:
                return True
            windowSet.add(nums[r])
            r += 1

            if r - l > k:
                windowSet.remove(nums[l])
                l += 1
        
        return False