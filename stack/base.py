# Stack tutorial


class Node:
    def __init__(self, value):
        self.value = value
        self.next_node = None

    def set_next_node(self, next_node):
        self.next_node = next

    def get_next_node(self):
        return self.next_node
    
    def get_value(self):
        return self.value
    

class Stack:
    def __init__(self, limit=10):
        self.top_item = None
        self.size = 0
        self.limit = limit

    def push(self, value):
        if self.has_space():
            item = Node(value)
            item.set_next_node(self.top_item)

            self.top_item = item
            self.size += 1

            print("Adding {} to the pizza stack!".format(value))
        else:
            print("No romm for {}!".format(value))
    
    def pop(self):
        if not self.is_empty():
            item_to_remove = self.top_item
            self.top_item = item_to_remove.get_next_node()
            self.size -= 1
            print("Delivering " + item_to_remove.get_value())

            return item_to_remove.get_value()
        print("All out of pizza.")

    def peek(self):
        if not self.is_empty():
            return self.top_item.get_value()
        print("Nothing to see here!")

    def has_space(self):
        return self.limit > self.size
    
    def is_empty(self):
        return self.size == 0
    
