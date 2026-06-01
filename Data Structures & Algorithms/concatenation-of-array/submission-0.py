class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = []
        length = len(nums)
        for i in range(2 * length):
            if i <= length-1:
                ans.append(nums[i])
            else:
                index = i - length
                ans.append(nums[index])
        return ans