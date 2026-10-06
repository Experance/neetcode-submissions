class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        char_counts = defaultdict(int)
        max_freq = 0
        start = 0

        for end in range(len(s)):
            char_counts[s[end]] += 1
            max_freq = max(max_freq, char_counts[s[end]])

            # If the current window is invalid, slide the left boundary forward by 1
            if (end - start + 1) - max_freq > k:
                char_counts[s[start]] -= 1
                start += 1

        return len(s) - start