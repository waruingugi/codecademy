# Bread First Search: Involves searching a tree level by level
# Key concepts are:
#   - Initialize a frontier queue which holds a path for each node to search
#   - Loop through the frontier queue to check if the node value matches the value we
#     are searching for.
#   - Continue the search by adding child nodes to the frontier until the goal has been found
#     or the tree has been completely searched.

from collections import deque


# Breadth-first search function
def bfs(root_node, goal_value):
    # Initialize frontier queue
    path_queue = deque()

    # Add rooth path to the frontier
    initial_path = [root_node]
    path_queue.appendleft(initial_path)

    # search loop that continues as long as there are path in the 
    # frontier
    while path_queue:
        # Get the next path and node
        # Then output node value
        current_path = path_queue.pop()
        current_node = current_path[-1]
        print(f"Searching node with value: {current_node.value}")

        # Check if the goal node is found
        if current_node.value == goal_value:
            return current_path
        
        # Add paths of children to the frontier
        for child in current_node.children:
            new_path = current_path[:]
            new_path.append(child)
            path_queue.appendleft(new_path)

    # Return an empty path if goal was not found
    return None
