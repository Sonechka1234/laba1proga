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

    def read_users(self):
        self.users = self.__storage.load_from_file("./db.xml")
        if not self.__users:
            print("База пользователей пуста.")
            return
        for user in self.__users:
            print(f"ID: {user.user_id}, Имя: {user.name}, Email: {user.email}, Возраст: {user.age}, Тип: {user.__class.name}")

    def update_user(self, user_type: str, user_id: int, name: str, email: str, age: int):
        self.users = self.__storage.load_from_file("./db.xml")
        for user in self.__users:
            if user.user_id == user_id and user.__class.name.lower() == user_type.lower():
                user.name = name
                user.email = email
                user.age = age
                self.storage.save_to_file(self.__users, "./db.xml")
                print("Пользователь успешно обновлен.")
                return
        print("Пользователь не найден.")

    def delete_user(self, user_type: str, user_id: int):
        self.__users = self.__storage.load_from_file("./db.xml")
        for user in self.__users:
            if user.user_id == user_id and user.__class.name.lower() == user_type.lower():
                self.__users.remove(user)
                self.__storage.save_to_file(self.__users, "./db.xml")
                print("Пользователь успешно удален.")
                return
        print("Пользователь не найден.")