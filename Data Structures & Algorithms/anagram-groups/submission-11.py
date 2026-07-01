from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # a map of sorted string to list of anagrams
        grouped = defaultdict(list)

        # loop through the list, populate in one pass
        for i, val in enumerate(strs):
            sorted_str = "".join(sorted(val))
            grouped[sorted_str].append(val)

        return list(grouped.values())


        