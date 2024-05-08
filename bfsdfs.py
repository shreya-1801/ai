def dfs(graph, start_node):
    visited = set()
    def dfs_util(node):
        if node not in visited:
            print(node)
            visited.add(node)
            for neighbour in graph[node]:
                dfs_util(neighbour)
    dfs_util(start_node)

def bfs(graph, start_node):
    visited = set()
    queue = []
    visited.add(start_node)
    queue.append(start_node)
    while queue:
        current_node = queue.pop(0)
        print(current_node, end=" ")
        for neighbour in graph[current_node]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)

graph = {}
num_edges = int(input("Enter the number of edges in the graph: "))
print("Enter the source & destination ofthe edges separated by space:")
for _ in range(num_edges):
    edge = input().split()
    source, destination = edge
    if source not in graph:
        graph[source] = []
    if destination not in graph:
        graph[destination] = []
    graph[source].append(destination)
    print(graph)

start_node_dfs = input("Enter the starting node for DFS: ")
print("Depth-First Search:")
dfs(graph, start_node_dfs)

start_node_bfs = input("Enter the starting node for BFS: ")
print("\nBreadth-First Search:")
bfs(graph, start_node_bfs)
