class Solution:
    def maxArea(self, heights: List[int]) -> int:
        def calculateWater(l, r):
            return min(heights[l], heights[r]) * (r - l)
        
            while heights[shorter] <= heights[taller]:
                shorter += 1 
        
        l, r = 0, len(heights) - 1
        maxWater = 0

        while l < r:
            maxWater = max(maxWater, calculateWater(l, r))

            if heights[l] <= heights[r]:
                l += 1
            else:
                r -= 1
            
        return maxWater