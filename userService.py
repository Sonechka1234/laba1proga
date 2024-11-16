from constants import USERS_FACTORY_MAP
from storage import Storage

class UserService:
    def __init__(self, storage: Storage) -> None:
        self.__storage = storage
        self.__users = []

    def create_user(self, user_type: str, user_id: int, name: str, email: str, age: int) -> None:
        if user_type not in USERS_FACTORY_MAP:
            raise TypeError
        user = USERS_FACTORY_MAP[user_type](user_id, name, email, age)
        self.__users.append(user)
        self.__storage.save_to_file(self.__users)

    def read_users(self) -> None:
        self.__users = self.__storage.load_from_file()
        if not self.__users:
            print("База пользователей пуста.")
            return
        for user in self.__users:
            print(f"ID: { user.user_id }, Имя: { user.name }, Email: { user.email }, Возраст: { user.age }, Тип: { user.__class__.__name__ }")

    def update_user(self, user_id: int, name: str, email: str, age: int) -> None:
        self.__users = self.__storage.load_from_file()
        for user in self.__users:
            if user.user_id == user_id:
                user.name = name
                user.email = email
                user.age = age
                self.__storage.save_to_file(self.__users)
                print("Пользователь успешно обновлен.")
                return
        print("Пользователь не найден.")

    def delete_user(self, user_id: int) -> None:
        self.__users = self.__storage.load_from_file()
        for user in self.__users:
            if user.user_id == user_id:
                self.__users.remove(user)
                self.__storage.save_to_file(self.__users)
                print("Пользователь успешно удален.")
                return
        print("Пользователь не найден.")