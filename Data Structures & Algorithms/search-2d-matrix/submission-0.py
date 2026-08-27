class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # first need to find which row using binary search
        
        l, r = 0, len(matrix) - 1

        while l <= r:
            m = l + (r - l) // 2
            
            if matrix[m][0] > target:
                r = m - 1
            elif matrix[m][0] < target:
                l = m + 1
            else:
                return True

        # after the first binary search, if the target has not been found,
        # the row we should then search through is at index (l - 1)

        row = matrix[l - 1]

        l, r = 0, len(row) - 1

        while l <= r:
            m = l + (r - l) // 2

            if row[m] > target:
                r = m - 1
            elif row[m] < target:
                l = m + 1
            else:
                return True

        return False 