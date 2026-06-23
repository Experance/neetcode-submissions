class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_dict = {}
        for i in range(len(nums)):
            nums_dict[nums[i]] = i

        for i in range(len(nums)):
            curr_add = target - nums[i]
            if curr_add in nums_dict and nums_dict[curr_add] != i:
                return [i, nums_dict[curr_add]]
        return []  
                


