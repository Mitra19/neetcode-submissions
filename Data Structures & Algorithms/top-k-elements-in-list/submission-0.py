from collections import Counter
from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_list = Counter(nums)
        ans = []
        for key, value in count_list.most_common(k):
            ans.append(key)   # ✅ append the number itself, not the frequency
        return ans
