class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        mx = max(piles)

        l, r = 1, mx
        k = mx

        while l <= r:
            m = l + (r - l) // 2

            numHours = self.eatingDuration(piles, m)

            if numHours <= h:
                k = min(k, m)
                r = m - 1
            elif numHours > h:
                l = m + 1
        
        return k

    def eatingDuration(self, piles: List[int], m: int) -> int:
        duration = 0
        for p in piles:
            duration += math.ceil(p / m)
        
        return duration