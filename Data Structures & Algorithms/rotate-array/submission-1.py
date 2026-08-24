class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        rotated = [0] * len(nums)

        k = k % len(nums)

        for i in range(len(nums)):
            newIndex = (i + k) % len(nums)
            rotated[newIndex] = nums[i]

        for r in range(len(rotated)):
            nums[r] = rotated[r]
        
        