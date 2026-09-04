class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort()
        shortest = strs[0]
        longest = strs[-1]

        prefix = []
        for i in range(len(shortest)):
            if longest[i] != shortest[i]:
                return "".join(prefix)
            prefix.append(shortest[i])
        
        return "".join(prefix)