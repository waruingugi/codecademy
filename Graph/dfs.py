# Depth first search in graphs
# Can be a function or a class method


def dfs(graph, current_vertex, target_value, visited=None):
    if visited is None:
        visited = []

    visited.append(current_vertex)
    if current_vertex is target_value:
        return visited
    
    for neighbor in graph[current_vertex]:
        if neighbor not in visited:
            path = dfs(
                graph, neighbor, target_value, visited
            )
            if path: return path


some_hazardous_graph = {
    'lava': set(['sharks', 'piranhas']),
    'sharks': set(['piranhas', 'bees']),
    'piranhas': set(['bees']),
    'bees': set(['lasers']),
    'lasers': set([])
}
print(dfs(
    some_hazardous_graph, 'sharks', 'bees'
))