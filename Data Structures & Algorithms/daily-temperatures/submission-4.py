class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        pendingDays = [] # the indices of days that are missing a warmer day
        result = [0] * len(temperatures)
        
        for i, temp in enumerate(temperatures):
            while pendingDays and temp > temperatures[pendingDays[-1]]:
                day = pendingDays.pop()
                result[day] = i - day
            pendingDays.append(i)
        
        return result