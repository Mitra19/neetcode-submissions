class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 2:
            return max(nums)
        dp = [0] * n

        dp[0], dp[1] =nums[0], max(nums[0], nums[1])
        
        i = 2
        while i < n:
            dp[i] = max(nums[i]+dp[i-2], dp[i-1])
            i+=1
        print(f"dp: {dp}")
        return dp[-1]