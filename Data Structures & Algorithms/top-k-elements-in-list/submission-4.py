class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # create a dict where the key is the number of items, and value is a list of all numbers with much
        # Finally loop through k through the values starting from the largest key

        mapped_nums = defaultdict(list)

        nums.sort()

        prior_val = nums[0]
        counter = 0
        for num in nums:
            if (num == prior_val):
                counter += 1
            else:
                mapped_nums[counter].append(prior_val)
                counter = 1
                prior_val = num

        mapped_nums[counter].append(prior_val)

        output_vals = []
        mapped_nums_keys = sorted(mapped_nums.keys(), reverse=True)
        print(mapped_nums.keys())
        # loop through k values
        for i in mapped_nums_keys:
            for val in mapped_nums[i]:
                if k == 0:
                    print(output_vals)
                    return output_vals
                else: 
                    print(val)
                    output_vals.append(val)
                    k -= 1

        return output_vals
