from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # count frequencies, create hashmap of frequency -> value
        # then sort values based on their corresponding frequencies
        # take topk of them
        # 

        # fill out hashmap
        top_k = defaultdict(int)
        for num in nums:
            top_k[num] = top_k[num] + 1
        
        # create pairs of frequency and corresponding value
        arr = []
        for num, count in top_k.items():
            arr.append([count, num])

        # sort based on frequency
        arr.sort(reverse=True)
        # now add top k vals!
        val_list = []
        for i in range(len(arr)):
            if i == k:
                return val_list
            else:
                val_list.append(arr[i][1])

            
        return val_list
