class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        count = Counter(nums).most_common()
        ans = []
        print(count)
        for num, times in count:
            while times:
                ans.append(num)
                times -= 1
        return ans[::-1]