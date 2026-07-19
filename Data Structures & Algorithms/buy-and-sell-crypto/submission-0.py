class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maximum = 0
        minimum = float("inf")
        ans = 0
        for price in prices:
            minimum = min(minimum, price)
            ans = max(price - minimum, ans)
        print(f"max: {maximum} min: {minimum}")
        return ans