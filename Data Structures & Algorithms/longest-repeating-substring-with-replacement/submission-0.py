class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l, r = 0, 0
        longest = 0
        windowChars = [0] * 26
        maxFreq = 0

        for r in range(len(s)):
            windowChars[ord(s[r]) - ord('A')] += 1
            maxFreq = max(maxFreq, windowChars[ord(s[r]) - ord('A')])

            if (r - l + 1) - maxFreq > k:
                windowChars[ord(s[l]) - ord('A')] -= 1
                l += 1
            
            longest = max(longest, r - l + 1)
        
        return longest