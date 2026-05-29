class Solution:

    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums = sorted(nums)
        ans = []
        for index in range(len(nums)):
            # print(f"index: {index}")
            if index > 0 and nums[index] == nums[index-1]:
                continue
            else:
                    l, r = index+1, len(nums)-1
                    while(l<r):
                        sum = nums[index] + nums[l] + nums[r]
                        if(sum > 0):
                            r-=1
                        elif sum < 0:
                            l+=1
                        elif sum == 0:
                            ans.append([nums[index] ,nums[l] , nums[r]])
                            l +=1
                            r-=1
                            while l < r and nums[l] == nums[l-1]:
                                l += 1
                            # skip duplicates on right
                            while l < r and nums[r] == nums[r+1]:
                                r -= 1
        return ans