from project.id_mixin import IdMixin


class ExercisePlan(IdMixin):
    def __init__(self, trainer_id: int, equipment_id: int, duration: int):
        self.duration = duration
        self.equipment_id = equipment_id
        self.trainer_id = trainer_id
        self.id = self.get_next_id()
        self.increment_ID()

    @classmethod
    def from_hours(cls, trainer_id:int, equipment_id:int, hours:int):
        minutes = hours // 60
        return cls(trainer_id, equipment_id, minutes)

    def __repr__(self):
        return f"Plan <{self.id}> with duration {self.duration} minutes"
