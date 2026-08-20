class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort() # O(log(n))
        triplets = []

        for i in range(len(nums) - 2): # (O(n))
            if nums[i] > 0:
                break

            if i > 0 and nums[i - 1] == nums[i]:
                continue

            target = 0 - nums[i]
            l, r = i + 1, len(nums) - 1

            while l < r:
                if nums[l] + nums[r] == target:
                    triplets.append([nums[i], nums[l], nums[r]])
                    l += 1                    
                    r -= 1

                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                elif nums[l] + nums[r] > target:
                    r -= 1
                else:
                    l += 1

        return triplets