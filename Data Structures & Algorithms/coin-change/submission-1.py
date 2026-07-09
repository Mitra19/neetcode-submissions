from typing import List
from functools import lru_cache

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        # @lru_cache(None)  # Caches results to avoid Time Limit Exceeded (TLE)
        def dfs(rem_amount: int) -> float:
            # Base cases
            if rem_amount == 0:
                return 0
            if rem_amount < 0:
                return float('inf')
            
            min_coins = float('inf')
            
            # Try every coin option for the current remaining amount
            for coin in coins:
                res = dfs(rem_amount - coin)
                if res != float('inf'):
                    min_coins = min(min_coins, res + 1)
            
            return min_coins
        
        ans = dfs(amount)
        return ans if ans != float('inf') else -1
