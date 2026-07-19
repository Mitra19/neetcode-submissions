class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minimum = float("inf")
        ans = 0
        for price in prices:
            minimum = min(minimum, price)
            ans = max(price - minimum, ans)
        return ans