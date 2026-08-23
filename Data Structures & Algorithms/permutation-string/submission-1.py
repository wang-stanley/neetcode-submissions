class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1Count = [0] * 26

        for c in s1:
            s1Count[ord(c) - ord('a')] += 1
        

        l, r = 0, 0
        windowCount = [0] * 26

        for r in range(len(s2)):
            chIndex = ord(s2[r]) - ord('a')
            windowCount[chIndex] += 1

            while windowCount[chIndex] > s1Count[chIndex]:
                windowCount[ord(s2[l]) - ord('a')] -= 1
                l += 1
            
            if r - l + 1 == len(s1):
                return True
        
        return False