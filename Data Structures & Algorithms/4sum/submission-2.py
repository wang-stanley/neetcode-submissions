class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        print(f"nums: {nums}")

        result = []

        for i in range(0, len(nums) - 3):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            for j in range(i + 1, len(nums) - 2):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue

                twoSum = nums[i] + nums[j]
                diff = target - twoSum

                l, r = j + 1, len(nums) - 1

                while l < r:
                    if nums[l] + nums[r] < diff:
                        l += 1
                    elif nums[l] + nums[r] > diff:
                        r -= 1
                    else:
                        result.append([nums[i], nums[j], nums[l], nums[r]])
                        l += 1
                        r -= 1

                        while l < r and nums[l - 1] == nums[l]:
                            l += 1
                        while l < r and nums[r + 1] == nums[r]:
                            r -= 1
        
        return result