class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        w = set()
        max_length = 0
        l = 0
        count = 0

        for r in range(len(s)):
            while s[r] in w:
                w.remove(s[l])
                l += 1
            
            if s[r] not in w:
                w.add(s[r])

            max_length = max(max_length, r - l + 1)
        
        return max_length

