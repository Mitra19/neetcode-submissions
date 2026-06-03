class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        count = Counter(nums)

        def get_key(x):
            return (count[x], -x)

        return sorted(nums, key=get_key)