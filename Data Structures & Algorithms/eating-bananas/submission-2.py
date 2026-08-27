class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # need to eat all the piles in h hours
        # fastest rate you can eat all the bananas is the max value of all the piles
        # since then you guarantee eating all piles in one hour

        # Can perform a binary search with bounds [1, max] representing eating rate
        # and calculate the amount of time it takes to eat at that rate by looping over piles.

        # If it's lower than h, we have a valid k and we decrease the right bound to try a lower rate.
        # If it's greater than h, then we don't have a valid k and we need to increase the left bound
        # to try a higher eating rate.

        # When the binary search ends, we'll have tried the minumum rate that satisfies
        # the time h.

        # For each k value that we try, we iterate over piles (length n). We try log(n) k values,
        # so the total time complexity is O(nlog(n)).

        l, r = 1, max(piles)
        k = r

        while l <= r:
            m = l + (r - l) // 2
            duration = 0
            for p in piles:
                duration += math.ceil(p / m)
            if duration <= h:
                k = m
                r = m - 1
            else:
                l = m + 1
        
        return k