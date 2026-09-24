class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        
        # perform two pointer inside a loop that goes through the whole list
        final_list = []
        final_set = set()
        for i in range(len(nums)):
            target = 0 - nums[i]
            # now do two pointer on the target with the rest of the possible combos
            start = i + 1
            end = len(nums) - 1
            while start < end:
                if nums[start] + nums[end] > target:
                    end -= 1
                elif nums[start] + nums[end] < target:
                    start += 1
                else:
                    if (nums[i], nums[start], nums[end]) not in final_set:
                        final_set.add((nums[i], nums[start], nums[end]))
                        final_list.append([nums[i], nums[start], nums[end]])
                    start += 1

        return final_list