from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        water_cap = 0
        n = len(height)
        if n <= 2:
            return 0

        l, r = 0, n - 1
        max_left = 0
        max_right = 0

        # Move the smaller side inward and accumulate trapped water
        while l <= r:
            if height[l] <= height[r]:
                if height[l] >= max_left:
                    max_left = height[l]
                else:
                    water_cap += max_left - height[l]
                l += 1
            else:
                if height[r] >= max_right:
                    max_right = height[r]
                else:
                    water_cap += max_right - height[r]
                r -= 1

        return water_cap
