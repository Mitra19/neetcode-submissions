class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result = 0
        for index in range(len(nums)):
            result = result ^ nums[index]
        return result