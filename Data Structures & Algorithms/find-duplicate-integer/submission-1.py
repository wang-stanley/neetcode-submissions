class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        s, f = 0, 0

        while True:
            s = nums[s]
            f = nums[nums[f]]

            if s == f:
                break

        p = 0
        
        while p != s:
            p = nums[p]
            s = nums[s]

        return p

# s = 1 3 2 4
# f = 3 4 4 4