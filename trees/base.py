# Trees: Nodes with a parent to child relationship
# Nodes hold any type of data inside value
# Nodes hold children as a list, which can be empty for the root node.
# TreeNodes can add or remove children from themselves.


class TreeNode:
    def __init__(self, value):
        self.value = value
        self.children = []

    def add_child(self, child_node):
        self.children.append(child_node)

    def remove_child(self, child_node):
        self.children = [
            child for child in self.children if child is not child_node
        ]

    def traverse(self):
        nodes_to_visit = [self]
        while len(nodes_to_visit) > 0:
            current_node = nodes_to_visit.pop()
            print(current_node.value)
            nodes_to_visit += current_node.children
