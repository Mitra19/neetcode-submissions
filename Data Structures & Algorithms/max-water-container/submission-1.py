class Solution:
    def maxArea(self, height: List[int]) -> int:
        maximum_area = 0
        l , r = 0 , len(height) - 1
        while(l<r):
            width = r - l
            h = min(height[l], height[r])
            maximum_area = max(maximum_area, h*width)
            if height[l] < height[r]:
                l+=1
            else:
                r-=1
        return maximum_area

        