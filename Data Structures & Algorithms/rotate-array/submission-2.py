class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        k = k % len(nums)

        count = 0
        start = 0

        while count < len(nums):
            curIndex = start
            prev = nums[start]
            
            while True:
                nextIndex = (curIndex + k) % len(nums)
                temp = nums[nextIndex]
                nums[nextIndex] = prev
                prev = temp
                curIndex = nextIndex
                count += 1

                if curIndex == start:
                    break
            
            start += 1
