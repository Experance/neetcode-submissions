class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # sort the two strings, if equal than are anagrams
        return "".join(sorted(s)) == "".join(sorted(t))