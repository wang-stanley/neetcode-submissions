class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0

        l = 0
        seenChars = set()
        longest = 1

        for r in range(len(s)):
            if s[r] in seenChars:
                while s[r] in seenChars:
                    seenChars.remove(s[l])
                    l += 1
                seenChars.add(s[r])
            else:
                seenChars.add(s[r])
                longest = max(longest, r - l + 1)
        
        return longest