class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()

        l, r = 0, len(people) - 1
        numBoats = 0

        while l < r:
            weight = people[l] + people[r]
            if weight <= limit:
                l += 1
            r -= 1
            numBoats += 1
        
        if l == r:
            numBoats += 1

        return numBoats