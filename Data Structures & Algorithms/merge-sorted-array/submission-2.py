class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        
        i1, i2 = m - 1, n - 1
        curIndex = len(nums1) - 1

        while i2 >= 0:
            if i1 >= 0 and nums1[i1] > nums2[i2]:
                nums1[curIndex] = nums1[i1]
                i1 -= 1
            else:
                nums1[curIndex] = nums2[i2]
                i2 -= 1
            curIndex -= 1
            
        