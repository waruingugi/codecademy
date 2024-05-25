# Queue example


class User:
    def __init__(self, name):
        self.name = name
        self.next_user = None

    def set_next_user(self, user):
        self.next_user = user

    def get_next_user(self):
        return self.next_user
    
    def get_user_name(self):
        return self.name
    

class WaitingList:
    def __init__(self, max_size=3):
        self.max_size = max_size
        self.head = None
        self.tail = None
        self.current_size = 0

    def has_space(self):
        return self.current_size < self.max_size
    
    def get_size(self):
        return self.current_size
    
    def enqueue(self, name):
        if self.has_space():
            user = User(name)
            if self.get_size() == 0:
                self.head = user
                self.tail = user

            else:
                self.tail.set_next_user(user)
                self.tail = user
            
            self.current_size += 1
        return print(self.current_size)
    
    def dequeue(self):
        if self.get_size() == 1:
            self.head = None
            self.tail = None
            self.current_size -= 1

        elif self.get_size() == 0:
            pass

        else:
            current_head = self.head
            self.head = current_head.get_next_user()
            current_head.set_next_user(None)
            self.current_size -= 1

        return print(self.current_size)


maxwell = User("maxwell")
mark = User("mark")
tom = User("tom")
timmy = User("timmy")

waiting_list = WaitingList()
waiting_list.enqueue(maxwell)
waiting_list.enqueue(mark)
waiting_list.enqueue(tom)
waiting_list.enqueue(timmy)

waiting_list.dequeue()
waiting_list.dequeue()
waiting_list.dequeue()
waiting_list.dequeue()