class Solution:
    def findMin(self, nums: List[int]) -> int:
        # We know that there exists some pivot point in the array at which the start of the original
        # array begins. It is at that pivot point where we can find the minimum. But how do we find that?


        # When we do a binary search and have values (l, r, m), nums[m] follows one of either two cases:
        # nums[m] >= nums[l], in which we know they are one group and nums[r] is another
        # nums[m] < nums[l] in which we know nums[l] is one group and nums[m] and nums[r] are another

        # but first we should check if nums[l] > nums[r] to see if there's a rotation. If there is not a rotation
        # then nums[l] <= num[r] and we just check nums[l] and return.

        # Then, we know that there's a pivot point. If l+m are a group, then we should check the r group.
        # If l+r are a group, then we should check the left group

        l, r = 0, len(nums) - 1
        min_val = nums[0]

        while l <= r:
            if nums[l] <= nums[r]:
                min_val = min(min_val, nums[l])
                return min_val
            
            m = (l + r) // 2
            min_val = min(min_val, nums[m])
            if nums[m] >= nums[l]:
                l = m + 1
            else:
                r = m - 1
        
        return min_val