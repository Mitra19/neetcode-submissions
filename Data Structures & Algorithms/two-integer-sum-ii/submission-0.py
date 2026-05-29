import collections
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        nums_set = collections.defaultdict(int)
        for index,num in enumerate(nums):
            compliment = target - num
            if compliment in nums_set:
                return[nums_set[compliment]+1,index+1]
            nums_set[num] = index