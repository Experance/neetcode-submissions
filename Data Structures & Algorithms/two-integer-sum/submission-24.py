class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # create a map of all the values to corresponding index
        nums_map = {}

        for i in range(len(nums)):
            nums_map[nums[i]] = nums_map.get(nums[i], i)

        # then loop through each value, and check the opposite value, i.e.
        # target - curr and see if it exists in the map!
        for i, curr in enumerate(nums):
            other = target - curr
            if other in nums_map and nums_map[other] != i:
                return sorted([i, nums_map[other]])

        return []


