class User:
    def __init__(self, user_id: int, username: str):
        self.user_id = user_id
        self.username = username
        self.books = []

    def info(self):
        ordered_books = sorted(self.books)
        return ', '.join(ordered_books)

    def __str__(self):
        return {self.user_id}, {self.username}, {self.books}

