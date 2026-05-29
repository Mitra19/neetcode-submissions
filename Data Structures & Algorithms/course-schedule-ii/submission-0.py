class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        def dfs(src, adjList, path, visit, ans):
            if src in path:
                return False
            if src in visit:
                return True
            path.add(src)
            for neighbour in adjList[src]:
                if not dfs(neighbour, adjList, path, visit,ans):
                    return False
            path.remove(src)
            visit.add(src)
            ans.append(src)
            return True
        adjList = {}
        path, visit = set(), set()
        for i in range(numCourses):
            adjList[i] = []
            ans = []
        for [src, dest] in prerequisites:
            adjList[src].append(dest)
        for i in range(numCourses):
            if not dfs(i, adjList, path, visit, ans):
                return []
        return ans
