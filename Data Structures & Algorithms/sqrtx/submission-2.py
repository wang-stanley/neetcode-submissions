class Solution:
    def mySqrt(self, x: int) -> int:
        l, r = 1, x

        while l <= r:
            m = l + (r - l) // 2

            if m * m > x:
                r = m - 1
            elif m * m < x:
                l = m + 1 
            else:
                return m
        
        return r


# [1, 13]
# m = 7
# 7 * 7 = 49 > 13, so r = 6
# m = 1 + 2 = 3
# 3 * 3 = 9 < 13, so l = 4
# m = 4 + 1 = 5
# 5 * 5 = 25 > 13, so r = 4
# m = 4
# 4 * 4 = 16 > 13, so r = 3
