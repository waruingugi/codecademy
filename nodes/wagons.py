# Nodes practice
# Multiple wagons make up a train


class TrainWagon:
    def __init__(self, wagon_no, next_wagon=None):
        self.wagon_no = wagon_no
        self.next_wagon = next_wagon

    def set_next_wagon(self, next_wagon):
        self.next_wagon = next_wagon

    def get_next_wagon(self):
        return self.next_wagon
    
    def get_wagon_no(self):
        return self.wagon_no
    

wagon_one = TrainWagon(1)
wagon_two = TrainWagon(2)
wagon_three = TrainWagon(3)
wagon_one.set_next_wagon(wagon_two)
wagon_two.set_next_wagon(wagon_three)

print(f"Wagon three no: {wagon_two.get_next_wagon().get_wagon_no()}")