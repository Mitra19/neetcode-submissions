class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        ans = 0
        n = len(nums)
        for i in range(1,n+1):
            ans ^= i
        for i in range(n):
            ans ^= nums[i]
        return ans