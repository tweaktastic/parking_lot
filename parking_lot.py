class Car(object):

    def __init__(self, reg_number, color):
        self.reg_number = reg_number
        self.color = color


class ParkingLot(object):

    def __init__(self, size):
        self.size = size
        self.allocated_slots = dict()
        self.generate_slots()

    def generate_slots(self):
        self.available_slots = []
        for i in range(1, self.size+1):
            self.available_slots.push(i)

    def check_slots_available(self):
        return self.available_slots == 0

    def get_available_slot(self):
        # return the poped element from available_slots

    def assign_slot(self, reg_number, color):
        if self.check_slots_available():
            car = Car(reg_number, color)
            slot = self.get_available_slot()
            self.allocated_slots[slot] = car
            return True
        else:
            return "Slot not available"

    def remove_car(self, reg_number):
        found = False
        for k in self.allocated_slots.keys():
            if self.allocated_slots[k].reg_number == reg_number:
                found = True
                del self.allocated_slots[key]
                self.available_slots.push(int(key))
