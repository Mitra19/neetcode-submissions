class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        M, N = len(text1), len(text2)
        cache = [[-1] * N for i in range(M)]
        def memoization(str1, str2, l1, l2, cache):
            if l1 == len(str1) or l2 == len(str2):
                return 0
            if cache[l1][l2] != -1:
                return cache[l1][l2]
            if str1[l1] == str2[l2]:
                cache[l1][l2] = 1 + memoization(str1,str2, l1+1, l2+1, cache)
            else:
                cache[l1][l2] = max(memoization(str1,str2, l1+1,l2, cache), memoization(str1,str2, l1, l2+1, cache))
            return cache[l1][l2]
        return memoization(text1, text2, 0 , 0, cache)