from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # each sublist is a hashmap --> can use python's .values() function of dicts
        # use sorted for each key of string
        grouped_agrms = defaultdict(list)

        for s in strs:
            sorted_str = "".join(sorted(s))
            grouped_agrms[sorted_str].append(s)
        
        return list(grouped_agrms.values())