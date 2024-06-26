# Breadth first search in graphs
# Can be a function or a class method


def bfs(graph, start_vertex, target_value):
    path = [start_vertex]
    vertex_and_path = [start_vertex, path]

    bfs_queue = [vertex_and_path]
    visited = set()

    while bfs_queue:
        current_vertex, path = bfs_queue.pop(0)
        visited.add(current_vertex)

        for neighbor in graph[current_vertex]:
            if neighbor not in visited:
                if neighbor is target_value:
                    return path + [neighbor]
                
                else:
                    bfs_queue.append(
                        [neighbor, path + [neighbor]]
                    )


some_hazardous_graph = {
    'lava': set(['sharks', 'piranhas']),
    'sharks': set(['piranhas', 'bees']),
    'piranhas': set(['bees']),
    'bees': set(['lasers']),
    'lasers': set([])
  }

print(bfs(some_hazardous_graph, 'sharks', 'bees'))
