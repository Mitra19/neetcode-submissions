class Solution:
    def topologicalSort(self, n: int, edges: List[List[int]]) -> List[int]:
        def dfs(src, adjList, visit, path, ans):
            if src in path:
                return False
            if src in visit:
                return True
            visit.add(src)
            path.add(src)
            for neighbour in adjList[src]:
                if not dfs(neighbour, adjList, visit, path, ans):
                    return False
            path.remove(src)
            ans.append(src)
            return True
        adjList = {}
        for i in range(n):
            adjList[i] = []
        for [src, dsc] in edges:
            adjList[src].append(dsc)
        visit = set()
        path = set()
        ans = []
        for i in range(n):
            if not dfs(i, adjList, visit,path, ans):
                return []
        return ans[::-1]