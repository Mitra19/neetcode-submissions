class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        dp = {}
        def memoization(i, m, n):
            if i == len(strs):
                return 0
            if (i,m,n) in dp:
                return dp[(i,m,n)]
            dp[(i,m,n)] = memoization(i+1,m,n)
            m_count = strs[i].count("0")
            n_count = strs[i].count("1")
            if m_count <= m and n_count <= n:
                dp[(i,m,n)] = max(dp[(i,m,n)], 1 + memoization(i+1, m-m_count, n-n_count))
            return dp[(i,m,n)]
        return memoization(0,m,n)