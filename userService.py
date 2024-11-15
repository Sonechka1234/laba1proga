from constants import USERS_FACTORY_MAP
from storage import Storage


class UserService:
    def __init__(self, storage: Storage) -> None:
        self.__storage = storage
        self.__users = []
    def create_user(self, user_type: str, user_id: int, name: str, email: str, age: int):
        if user_type not in USERS_FACTORY_MAP:
            raise TypeError
        movie = USERS_FACTORY_MAP[user_type](user_id, name, email, age)
        self.__users.append(movie)
        self.__storage.save_to_file(self.__users, "./db.xml")

    def read_users(self, user_type: str, user_id: int, name: str, email: str, age: int):
        pass
    def update_user(self, user_type: str, user_id: int, name: str, email: str, age: int):
        pass
    def delete_user(self, user_type: str, user_id: int, name: str, email: str, age: int):
        pass