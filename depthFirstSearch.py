from pprint import pprint

def DFS(graph, node, discovered):
    process_node(node)
    for adjacent in graph[node]:
        if adjacent not in discovered:
            discovered[adjacent] = node
            DFS(graph, adjacent, discovered)

def process_node(node):
    print(f"Visiting node {node}")

def construct_path(u, v, discovered):
    path = []
    if v in discovered:
        path.append(v)
        walk = v
        while walk is not u:
            parent = discovered[walk]
            path.append(parent)
            walk = parent
        path.reverse()
    return path

def DFS_complete(graph):
    """Perform DFS for entire graph and return forest as a dictionary"""
    forest = {}
    for vertex in graph.keys():
        print(f"creating tree for node: {vertex}")
        if vertex not in forest:
            forest[vertex] = None
            DFS(graph, vertex, forest)
    return forest

if __name__ == '__main__':
    graph = {
        'A': ['B', 'C'],
        'B': ['D', 'E'],
        'C': ['F'],
        'D': [],
        'E': ['F'],
        'F': [],
        'G': ['H'],
        'H': ['G']
    }
    # # DFS
    # discovered = {'A': None}
    # DFS(graph, 'A', discovered)
    # print(f"discovered: {discovered}")

    # # Constructing path between nodes using DFS output
    # print("Path from A to F is: ", end="")
    # print(construct_path('A', 'F', discovered))

    # Creating forest of discovery trees for entire graph
    print("Constructing forest for entire graph...")
    print(DFS_complete(graph))
