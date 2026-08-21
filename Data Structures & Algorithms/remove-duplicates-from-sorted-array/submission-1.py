class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        numsSet = set(nums)
        k = len(numsSet)

        placementIndex = 0
        traversalIndex = 0
        while placementIndex < len(numsSet):
            if traversalIndex == 0 or nums[traversalIndex] != nums[traversalIndex - 1]:
                nums[placementIndex] = nums[traversalIndex]
                placementIndex += 1
            traversalIndex += 1


        return k