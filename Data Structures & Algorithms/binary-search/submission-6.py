class Solution:
    def binary_search(self, l: int, r: int, nums: List[int], target: int) -> int:
        if l > r:
            return -1

        mid = l + (r - l) // 2

        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            return self.binary_search(l, mid - 1, nums, target)
        else:
            return self.binary_search(mid + 1, r, nums, target)

    def search(self, nums: List[int], target: int) -> int:
        return self.binary_search(0, len(nums) - 1, nums, target)