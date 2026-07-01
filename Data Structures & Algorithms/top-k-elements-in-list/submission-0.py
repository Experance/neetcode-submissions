# from collections import defaultdict
from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # --> Brute force
        # loop through list, building a map that counts the top k...return accordingly
        # map is num of vals -> val
        # 

        sorted_data = [item for item, count in Counter(nums).most_common()]

        return sorted_data[:k] if len(sorted_data) >= k else sorted_data
