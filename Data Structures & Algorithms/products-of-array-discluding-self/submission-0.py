class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer = []
        for index, num in enumerate(nums):
            if num != 0:
                answer.append(math.prod(nums)//num )
            else:
                answer.append(math.prod(nums[0:index])*math.prod(nums[index+1:len(nums)]))
        return answer