class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        
        ROW, COL = len(profit), capacity
        cache = [[-1] * (COL+1) for i in range(ROW)]
        def memoization(i, profit, weight, capacity, cache):
            if i == len(profit):
                return 0
            if cache[i][capacity] != -1:
                return cache[i][capacity]
            cache[i][capacity] = memoization(i+1, profit, weight,capacity, cache)
            newCap = capacity - weight[i]
            if newCap >= 0:
                p = profit[i] + memoization(i+1, profit, weight, newCap, cache)
                cache[i][capacity] = max(cache[i][capacity], p)
            return cache[i][capacity] 
        return memoization(0,profit, weight,capacity,cache)