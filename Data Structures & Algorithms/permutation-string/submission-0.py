class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1, n2 = len(s1), len(s2)
        if n1 > n2:
            return False

        s1_counts = defaultdict(int)
        s2_counts = defaultdict(int)
        # Initialize frequency counts for s1 and the first window of s2
        for i in range(n1):
            s1_counts[s1[i]] += 1
            s2_counts[s2[i]] += 1

        if s1_counts == s2_counts:
            return True

        # Slide the window across s2
        for i in range(n1, n2):
            # Add new character on the right
            s2_counts[s2[i]] += 1
            # Remove outgoing character
            left_char = s2[i - n1]
            s2_counts[left_char] -= 1
            if s2_counts[left_char] == 0:
                del s2_counts[left_char]

            if s1_counts == s2_counts:
                return True

        return False