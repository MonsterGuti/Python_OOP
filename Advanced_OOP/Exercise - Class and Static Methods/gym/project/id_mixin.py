class IdMixin:
    id: int = 1

    @classmethod
    def get_next_id(cls):
        return cls.id

    @classmethod
    def increment_ID(cls):
        cls.id += 1
