class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        ans = float('inf')
        while(left <= right):
            mid = (left + right) // 2
            if nums[left] <= nums[mid]:
                ans =  min(nums[left], ans)
                left = mid + 1
            else:
                ans = min(nums[mid], ans)
                right = mid - 1
        return ans