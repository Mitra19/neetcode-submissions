class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        count = Counter(nums).most_common()
        ans = []
        print(count)
        times_sum = 0
        times_sum = count[0][1] == count[-1][1]
        for num, times in count:
            while times:
                ans.append(num)
                times -= 1
        return ans[::-1] if not times_sum else sorted(ans)[::-1]