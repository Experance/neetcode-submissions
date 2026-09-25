class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # have pointers at first 2 chars; shift right pointer until we get duplicate character; record max_val
        # shift left pointer, repeat
        if len(s) == 0: return 0
        if len(s) == 1: return 1

        l, r = 0, 1
        max_val = 1
        curr_string = set(s[l])

        while r < len(s):
            if s[r] in curr_string:
                max_val = max(max_val, r - l)
                curr_string.remove(s[l])
                l = l + 1
            else:
                curr_string.add(s[r])
                r += 1

        return max(max_val, r - l)
            
