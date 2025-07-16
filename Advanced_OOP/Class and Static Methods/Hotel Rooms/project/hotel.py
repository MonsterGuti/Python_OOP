from project.room import Room

class Hotel:
    def __init__(self, name: str):
        self.name = name
        self.rooms = []
        self.guests = 0

    @classmethod
    def from_stars(cls, stars_count: int):
        return cls(f"{stars_count} stars Hotel")

    def add_room(self, room: Room):
        self.rooms.append(room)

    def take_room(self, room_number, people):
        room = next((r for r in self.rooms if r.number == room_number), None)
        if room:
            result = room.take_room(people)
            if result is None:
                self.guests += people

    def free_room(self, room_number):
        room = next((r for r in self.rooms if r.number == room_number), None)
        if room and room.is_taken:
            self.guests -= room.guests
            room.free_room()

    def status(self):
        free_rooms = [str(r.number) for r in self.rooms if not r.is_taken]
        taken_rooms = [str(r.number) for r in self.rooms if r.is_taken]
        return (
            f"Hotel {self.name} has {self.guests} total guests\n"
            f"Free rooms: {', '.join(free_rooms)}\n"
            f"Taken rooms: {', '.join(taken_rooms)}"
        )
