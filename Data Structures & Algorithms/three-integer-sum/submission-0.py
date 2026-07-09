class Solution:
    def twoSum(self, duplicate_list:list[int], target: int) -> list[int]:
        l, r = 0, len(duplicate_list)-1

        while(l<r):
            if target > (duplicate_list[l] + duplicate_list[r]):
                l += 1
            if target < (duplicate_list[l] + duplicate_list[r]):
                r -= 1
            if target == duplicate_list[l] + duplicate_list[r]:
                answer = [duplicate_list[l],duplicate_list[r]]
                duplicate_list.remove(duplicate_list[r])
                if (l<r):
                    duplicate_list.remove(duplicate_list[l])
                return answer
        return None
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        ans = []
        sort_nums = sorted(nums)
        duplicate_list = sort_nums
        for index, num in enumerate(sort_nums):
            if index == len(nums) - 2:
                return ans
            else:
                duplicate_list.remove(num)
                answer_list = self.twoSum(duplicate_list, -num)
                if answer_list is not None:
                    answer_list.append(num)
                    ans.append(answer_list)
        return ans