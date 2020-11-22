from collections import deque

def bfs_print(graph, start_node):
    discovered = {start_node: None} # dictionary used to map vertex to edge used to discover it
    queue = deque()
    queue.append(start_node)
    while queue:
        # get adjacent nodes
        curr = queue.popleft()                          # pop oldest node
        process_node(curr)                              # perform some operation when visiting it
        for node in graph[curr]:                        # add all of its non-discovered adjacent nodes to queue
            if node not in discovered:
                discovered[node] = curr 
                queue.append(node)
             
def process_node(node):
    print(f"Visiting node {node}")


if __name__ == '__main__':
    graph = {
        'A': ['B', 'C'],
        'B': ['D', 'E'],
        'C': ['F'],
        'D': [],
        'E': ['F'],
        'F': []
    }
    bfs_print(graph, 'A')
