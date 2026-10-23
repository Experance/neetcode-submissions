class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0: return 0
        if len(s) == 1: return 1

        l, r = 0, 1

        max_len = 1
        unique_strs = set(s[l])

        while r < len(s):
            if s[r] in unique_strs:
                # remove from strs
                unique_strs.remove(s[l])
                max_len = max(max_len, r - l)
                l += 1
            else: 
                unique_strs.add(s[r])
                r += 1

        return max(max_len, r - l)