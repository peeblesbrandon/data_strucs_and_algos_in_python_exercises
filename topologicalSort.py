from collections import deque

class Solution:
    def topSort(self, edges):
        # build adjacency list
        graph = {}
        for edge in edges:
            if edge[0] not in graph:
                graph[edge[0]] = []
            if edge[1] not in graph:
                graph[edge[1]] = []
            graph[edge[0]].append(edge[1])
        # set up
        stack = deque()
        visited = set()
        # iterate through vertices
        for vertex in graph:
            if vertex not in visited:
                self.dfs(vertex, graph, visited, stack)
        stack = list(stack)
        stack.reverse()
        return stack

    def dfs(self, vertex, graph, visited, stack):
        visited.add(vertex)
        for adjacent in graph[vertex]:
            if adjacent not in visited:
                self.dfs(adjacent, graph, visited, stack)
        # once we've explored all adjacent (children) nodes
        stack.append(vertex)

if __name__ == "__main__":
    edges = [
        ['a', 'c'],
        ['b', 'c'],
        ['b', 'e'],
        ['c', 'd'],
        ['d', 'f'],
        ['f', 'g'],
        ['e', 'f']
    ]
    mySolution = Solution()
    print(mySolution.topSort(edges))
