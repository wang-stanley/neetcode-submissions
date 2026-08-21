class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 1, len(height) - 2
        lwall, rwall = height[0], height[-1]
        trapped = 0

        while l <= r:
            if lwall < rwall:
                if height[l] >= lwall:
                    lwall = height[l]
                else:
                    # print(f"Trapped water l: (l, r) = ({l}, {r})")
                    trapped += lwall - height[l]
                l += 1
            else:
                if height[r] >= rwall:
                    rwall = height[r]
                else:
                    # print(f"Trapped water r: (l, r) = ({l}, {r})")
                    trapped += rwall - height[r]
                r -= 1
        
        return trapped