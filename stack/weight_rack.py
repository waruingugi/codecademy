class DumbBell:
    def __init__(self, weight):
        self.weight = weight
        self.next_dumbell = None

    def set_next_dumbell(self, next_dumbell):
        self.next_dumbell = next_dumbell

    def get_next_dumbell(self):
        return self.next_dumbell
    
    def get_weight(self):
        return self.weight
    


class Rack:
    def __init__(self, limit=3):
        self.limit = limit
        self.top = None
        self.current_size = 0

    def has_space(self):
        return self.current_size < self.limit
    
    def is_empty(self):
        return self.current_size == 0
    
    def peek(self):
        if not self.is_empty():
            return self.top.get_weight()
        return print("Empty!")
    
    def push(self, weight):
        if self.has_space():
            dumbell = DumbBell(weight)
            dumbell.set_next_dumbell(self.top)
            self.top = dumbell

            self.current_size += 1
        
        return self.current_size
        
    def pop(self):
        if not self.is_empty():
            dumbell_to_remove = self.top
            self.top = dumbell_to_remove.get_next_dumbell()

            dumbell_to_remove.set_next_dumbell(None)

            return dumbell_to_remove.get_weight()
        

rack = Rack(3)
rack.push(5)
rack.push(7)
print(rack.push(8))
print(rack.push(10))

print(rack.peek())
print(rack.pop())
print(rack.peek())