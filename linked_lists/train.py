# LinkedList Practice


class Wagon:
    def __init__(self, number):
        self.wagon_number = number
        self.next_wagon = None
    
    def get_wagon_number(self):
        return self.wagon_number

    def set_next_wagon(self, wagon):
        self.next_wagon = wagon
    
    def get_next_wagon(self):
        return self.next_wagon


class Train:
    def __init__(self, train_name):
        self.train_name = train_name
        self.head_wagon = None
        self.tail_wagon = self.head_wagon


    def get_head_wagon(self):
        return self.head_wagon
    
    def add_wagon(self, wagon_number):
        wagon = Wagon(wagon_number)
        wagon.set_next_wagon(self.head_wagon)
        self.head_wagon = wagon

    def show_wagons(self):
        wagons = ""
        current_wagon = self.head_wagon
        while current_wagon is not None:
            wagons = wagons + current_wagon.get_wagon_number() + " -> "
            current_wagon = current_wagon.get_next_wagon()
        
        return wagons
    
    def remove_wagons(self, wagon_number):
        current_wagon = self.head_wagon

        if current_wagon.get_wagon_number() == wagon_number:
            self.head_wagon = self.head_wagon.get_next_wagon()

        else:
            next_wagon = current_wagon.get_next_wagon()
    
            while next_wagon:
                next_wagon_no = next_wagon.get_wagon_number()

                if next_wagon_no == wagon_number:
                    current_wagon.set_next_wagon(next_wagon.get_next_wagon())
                    next_wagon = None

                else:
                    current_wagon = next_wagon
                    next_wagon = current_wagon.get_next_wagon()


sgr_train = Train("SGR")
sgr_train.add_wagon("wagon_one")
sgr_train.add_wagon("wagon_two")
sgr_train.add_wagon("wagon_three")

print(f"Head wagon: {sgr_train.get_head_wagon().get_wagon_number()}")
print(sgr_train.show_wagons())

sgr_train.remove_wagons("wagon_three")
print(f"Updated wagon sequence: {sgr_train.show_wagons()}")
