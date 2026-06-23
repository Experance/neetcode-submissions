class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # loop through each string in list, and add to the overall list of lists.
        # Each new list in the list of lists get's it's sorted string as a key, and val
        # as index (hashmap)
        
        global_list = []
        str_to_index = {}
        i = 0
        for item in strs:
            new_str = "".join(sorted(item))
            str_to_index[new_str] = str_to_index.get(new_str, i)
            if len(global_list) == str_to_index[new_str]:
                global_list.append([item])
                i+=1
            else:
                global_list[str_to_index[new_str]].append(item)

        return global_list
        