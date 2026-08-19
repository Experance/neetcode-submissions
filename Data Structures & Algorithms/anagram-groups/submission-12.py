class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # loop through strs; check each and if the key of the map exists, then add it to the mapping
        # at the end return .values() of the map

        anagram_map = defaultdict(list)

        for str in strs:
            sorted_str = "".join(sorted(str))
            anagram_map[sorted_str].append(str)

        return list(anagram_map.values())

