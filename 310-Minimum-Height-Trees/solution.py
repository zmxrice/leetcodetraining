class Solution(object):
    def findMinHeightTrees(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        graph = [set() for i in xrange(n)]
        for x, y in edges:
            graph[x].add(y)
            graph[y].add(x)
        leaves = [i for i in xrange(n) if len(graph[i]) <= 1]
        while n > 2:
            newLeaves = []
            n -= len(leaves)
            for x in leaves:
                for y in graph[x]:
                    graph[y].remove(x)
                    if len(graph[y]) == 1:
                        newLeaves.append(y)
            leaves = newLeaves
        return leaves
            