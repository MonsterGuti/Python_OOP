from project import Library
from project import User

class Registration:

    @staticmethod
    def add_user(user: User, library: Library):
        if user not in library.user_records:
            library.user_records.append(user)
            return None
        return f"User with id = {user.user_id} already registered in the library!"

    @staticmethod
    def remove_user(user: User, library: Library):
        if user in library.user_records:
            library.user_records.remove(user)
            return None
        return "We could not find such user to remove!"

    @staticmethod
    def change_username(user_id: int, new_username: str, library: Library):
        user = next((u for u in library.user_records if u.user_id == user_id), None)
        if user is None:
            return f"There is no user with id = {user_id}!"

        if user.username == new_username:
            return "Please check again the provided username - it should be different than the username used so far!"

        if user.username in library.rented_books:
            library.rented_books[new_username] = library.rented_books[user.username]
            del library.rented_books[user.username]

        user.username = new_username
        return f"Username successfully changed to: {new_username} for user id: {user_id}"
