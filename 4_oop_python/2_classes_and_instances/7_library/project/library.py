class Library:
    def __init__(self):
        self.user_records = []
        self.books_available = {}
        self.rented_books = {}

    def add_user(self, user):
        if user.user_id not in self.user_records:
            self.user_records.append(user)
        else:
            return f'User with id = {user.user_id}' \
                   f' already registered in the library!'

    def remove_user(self, user):
        if user in self.user_records:
            self.user_records.remove(user)
        else:
            return f'We could not find such user to remove!'

    def change_username(self, user_id: int, new_username: str):
        users = list(filter(lambda user: user.user_id == user_id, self.user_records))
        if users:
            if users[0].username != new_username:
                return f'Username successfully changed to:' \
                       f' {new_username} for userid: {user_id}'
            else:
                return f'Please check again the provided username - ' \
                       f'it should be different than the username used so far!'
        else:
            return f'There is no user with id = {user_id}!'

