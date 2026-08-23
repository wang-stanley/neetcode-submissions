class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        l = 0
        r = k - 1

        if k == len(arr):
            return arr
            

        while r < len(arr) - 1 and self.isCloser(arr[r + 1], arr[l], x):
            l += 1
            r += 1
        
        return arr[l:r + 1]


    def isCloser(self, n1: int, n2: int, x: int) -> bool:
        if abs(n1 - x) < abs(n2 - x):
            return True
        if abs(n1 - x) == abs(n2 - x) and n1 <= n2:
            return True
        return False


