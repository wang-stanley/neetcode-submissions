class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        # we maintain some kind of queue of maxes that is intialized by first iterating over the 
        # first k elements of nums

        # since the array can have duplicates, I'm guessing that we store indices instead of values

        # as we slide this fixed window along the array, if our new right element that we encounter is
        # greater than the front? (back?) of the queue,

        q = deque([0])

        l = 0

        result = []
        print("q:", q)

        for r in range(len(nums)):
            while q and q[0] < (r - k + 1):
                q.popleft()
            
            if q and nums[r] > nums[q[0]]:
                q.appendleft(r)
            else:
                while q and nums[r] > nums[q[-1]]:
                    q.pop()
                q.append(r)
            
            if r >= k - 1:
                result.append(nums[q[0]])

        
        return result