# Depth first search uses recursive method to search for a path to a node.
# Uses tuples, which are immutable lists
# The DFS function returns none if no path is found


def dfs(root, target, path=()):
    path = path + (root, )

    if root.value == target:
        return path
    
    for child in root.children:
        path_found = dfs(child, target, path)

        if path_found is not  None:
            return path_found
        
    return None
