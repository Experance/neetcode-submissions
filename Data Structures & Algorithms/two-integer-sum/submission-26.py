class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # target - val = other_val --> build a mapping that tells us the index of each value (val -> index)
        # Then iterate through values, each time checking if other_val is in list!

        #build map
        val_to_index = {val : index for index, val in enumerate(nums)}

        for i, val in enumerate(nums):
            other_val = target - val
            if other_val in nums and i != val_to_index[other_val]:
                return [i, val_to_index[other_val]]
        
        return []
            

