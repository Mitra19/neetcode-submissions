class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [0 , 1]
        i = 2
        while i<= n+1:
            tmp = dp[1]
            dp[1] = dp[1] + dp[0]
            dp[0] = tmp
            i+=1
        return dp[1]  