# Double linkedlist example


class Wagon:
    def __init__(self, name):
        self.wagon_name = name
        self.next_wagon = None
        self.prev_wagon = None

    def get_wagon_name(self):
        return self.wagon_name
    
    def set_wagon_name(self, new_name):
        self.wagon_name = new_name
        return self.wagon_name
    
    def set_next_wagon(self, wagon):
        self.next_wagon = wagon
        return self.next_wagon
    
    def get_next_wagon(self):
        return self.next_wagon
    
    def set_prev_wagon(self, wagon):
        self.prev_wagon = wagon
        return self.prev_wagon
    
    def get_prev_wagon(self):
        return self.prev_wagon


class Train:
    def __init__(self, name):
        self.train_name = name
        self.head_wagon = None
        self.tail_wagon = None

    def set_head_wagon(self, wagon_name):
        new_wagon = Wagon(wagon_name)

        if self.head_wagon is None:
            self.head_wagon = new_wagon
            self.tail_wagon = new_wagon

        else:
            new_wagon.set_next_wagon(self.head_wagon)
            self.head_wagon.set_prev_wagon(new_wagon)
            self.head_wagon = new_wagon

        return self.head_wagon.get_wagon_name()
    
    def set_tail_wagon(self, wagon_name):
        new_wagon = Wagon(wagon_name)

        if self.tail_wagon is  None:
            self.head_wagon = new_wagon
            self.tail_wagon = new_wagon
        else:
            new_wagon.set_prev_wagon(self.tail_wagon)
            self.tail_wagon.set_next_wagon(new_wagon)
            self.tail_wagon = new_wagon

        return self.tail_wagon
    
    def remove_wagon(self, rm_wagon_name):
        current_wagon = self.head_wagon

        while current_wagon:
            
            if current_wagon.get_wagon_name() == rm_wagon_name:
    
                if current_wagon == self.head_wagon:
                    self.head_wagon = current_wagon.get_next_wagon()
                    self.head_wagon.set_prev_wagon(None)
                    current_wagon.set_next_wagon(None)
                    break

                elif current_wagon == self.tail_wagon:
                    self.tail_wagon = current_wagon.get_prev_wagon()
                    self.tail_wagon.set_next_wagon(None)
                    current_wagon.set_prev_wagon(None)
                    break

                else:
                    next_wagon = current_wagon.get_next_wagon()
                    prev_wagon = current_wagon.get_prev_wagon()
                    prev_wagon.set_next_wagon(next_wagon)
                    next_wagon.set_prev_wagon(prev_wagon)
                    break

            current_wagon = current_wagon.get_next_wagon()
            
    def get_head_wagon(self):
        return self.head_wagon.get_wagon_name()
    
    def get_tail_wagon(self):
        return self.tail_wagon.get_wagon_name()

    def show_wagons(self):
        current_wagon = self.head_wagon
        wagons = ""

        while current_wagon:
            wagons = wagons + " -> " + current_wagon.get_wagon_name()
            current_wagon = current_wagon.get_next_wagon()

        return wagons

sgr_train = Train("SGR")
sgr_train.set_head_wagon("wagon_one")
sgr_train.set_head_wagon("wagon_two")
sgr_train.set_head_wagon("wagon_three")

print(f"SGR train: {sgr_train.show_wagons()}")

chuchu_train = Train("Chuchu")
chuchu_train.set_tail_wagon("wagon_one")
chuchu_train.set_tail_wagon("wagon_two")
chuchu_train.set_head_wagon("wagon_three")
chuchu_train.set_tail_wagon("wagon_four")

print(f"Chuchu train: {chuchu_train.show_wagons()}")
chuchu_train.remove_wagon("wagon_three")
print(f"Chuchu train: {chuchu_train.show_wagons()}")
print(f"Chuchu train head wagon: {chuchu_train.get_head_wagon()}")
print(f"Chuchu train tail wagon: {chuchu_train.get_tail_wagon()}")