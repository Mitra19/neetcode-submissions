class Solution:
    def trap(self, height: list[int]) -> int:
        water_cap = 0
        n = len(height)
        max_left = [0] * n
        max_right = [0] * n
        left = height[0]
        right = height[n-1]
        for index in range(n):
            if(index > 0):
                max_left[index] = max(max_left[index-1], left)
                left = height[index]
            if(index < n-1):
                max_right[n-2-index] = max(max_right[n-1-index], right)
                right = height[n-2-index]
        print(f"max_left: {max_left}")
        print(f"max_right: {max_right}")
        for index in range(n):
            sum = min(max_left[index], max_right[index]) - height[index]
            water_cap += sum if sum>0 else 0
        return water_cap