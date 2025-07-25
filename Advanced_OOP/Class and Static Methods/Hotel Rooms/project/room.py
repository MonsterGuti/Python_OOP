class Room:
    def __init__(self, number: int, capacity: int):
        self.number = number
        self.capacity = capacity
        self.guests = 0
        self.is_taken = False

    def take_room(self, people):
        if not self.is_taken and people <= self.capacity:
            self.guests = people
            self.is_taken = True
            return None
        return f"Room number {self.number} cannot be taken"

    def free_room(self):
        if not self.is_taken:
            return f"Room number {self.number} is not taken"
        self.guests = 0
        self.is_taken = False
        return None
