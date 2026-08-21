class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # leftWalls[i] = index of the next shortest height to the left of index i
        # rightWalls[i] = index of the next shortest height to the right of index i
        leftWalls, rightWalls = [-1] * len(heights), [len(heights)] * len(heights)

        missingWalls = []

        for i, h in enumerate(heights):
            while missingWalls and heights[missingWalls[-1]] > h:
                rightWalls[missingWalls.pop()] = i

            missingWalls.append(i)

        missingWalls.clear()
        for i in range(len(heights) - 1, -1, -1):
            h = heights[i]
            while missingWalls and heights[missingWalls[-1]] > h:
                leftWalls[missingWalls.pop()] = i
            
            missingWalls.append(i)

        maxArea = 0

        for i, h in enumerate(heights):
            curArea = h * (rightWalls[i] - leftWalls[i] - 1)
            maxArea = max(maxArea, curArea)

        return maxArea