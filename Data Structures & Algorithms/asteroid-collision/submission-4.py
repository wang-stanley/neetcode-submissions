class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        result = []

        for a in asteroids:
            if a > 0:
                result.append(a)
                continue

            while result and result[-1] > 0 and abs(a) > result[-1]:
                result.pop()
            if result and abs(a) == result[-1]:
                result.pop()
            elif not result or result[-1] < 0 or abs(a) == result[-1]:
                result.append(a)

        return result
