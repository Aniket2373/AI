def dfs(graph, start_node, visited):
    visited[start_node] = True
    print(start_node)

    for neighbor in graph[start_node]:
        if not visited[neighbor]:
            dfs(graph, neighbor, visited)

def bfs(graph, start_node):
    queue = [start_node]
    visited = [False] * len(graph)  # Initialize visited list

    visited[start_node] = True  # Mark start_node as visited

    while queue:
        current = queue.pop(0)
        print(current)

        for neighbor in graph[current]:
            if not visited[neighbor]:
                queue.append(neighbor)
                visited[neighbor] = True  # Mark neighbor as visited

def main():
    graph = {}
    num_nodes = int(input("Enter the number of nodes: "))

    # Input graph edges
    for i in range(num_nodes):
        neighbors = list(map(int, input(f"Enter neighbors for node {i}: ").split()))
        graph[i] = neighbors

    start_node = int(input("Enter the starting node: "))

    traversal_type = input("Enter 'dfs' for Depth-First Search or 'bfs' for Breadth-First Search: ")

    if traversal_type.lower() == 'dfs':
        print("DFS Traversal:")
        visited_dfs = [False] * num_nodes  # Initialize visited list for DFS
        dfs(graph, start_node, visited_dfs)
    elif traversal_type.lower() == 'bfs':
        print("BFS Traversal:")
        bfs(graph, start_node)
    else:
        print("Invalid traversal type. Please enter 'dfs' or 'bfs'.")
        
main()
# if __name__ == "__main__":
#     main()


# Enter the number of nodes: 7
# Enter neighbors for node 0: 1 2 
# Enter neighbors for node 1: 3 4 
# Enter neighbors for node 2: 5 6 
# Enter neighbors for node 3: 1 
# Enter neighbors for node 4: 1
# Enter neighbors for node 5: 2
# Enter neighbors for node 6: 2
# Enter the starting node: 0