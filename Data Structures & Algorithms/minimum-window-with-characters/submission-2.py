class Solution:
    def minWindow(self, s: str, t: str) -> str:
        l = 0
        shortest = ""

        tCount = {}

        for ch in t:
            if ch not in tCount:
                tCount[ch] = 0
            tCount[ch] += 1

        windowCount = {}
        charsMatched = 0
        for r in range(len(s)):
            if s[r] in tCount:
                # character is part of t
                if s[r] not in windowCount:
                    windowCount[s[r]] = 0
                windowCount[s[r]] += 1

                if windowCount[s[r]] == tCount[s[r]]:
                    charsMatched += 1
                
                while charsMatched == len(tCount):
                    if shortest == "" or len(shortest) > (r - l + 1):
                        shortest = s[l:r + 1]
                    
                    if s[l] in tCount:
                        windowCount[s[l]] -= 1

                        if windowCount[s[l]] == tCount[s[l]] - 1:
                            charsMatched -= 1
                        
                    l += 1

        return shortest
