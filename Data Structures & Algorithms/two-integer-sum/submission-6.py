class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        answer_set = {}
        for index in range(len(nums)):
            complement = target - nums[index]
            if complement in answer_set:
                return[answer_set[complement], index]
            answer_set[nums[index]]=index
        return None