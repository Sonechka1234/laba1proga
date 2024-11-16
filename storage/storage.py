from utils import USERS_FACTORY_MAP
from storage.serializer import Serializer

class Storage:
    def __init__(self, serializer: Serializer, file_path: str):
        self.__serializer = serializer
        self.__file_path = f'{file_path}.{serializer.get_format()}'

    def save_to_file(self, data: dict) -> None:
        serialized_data = self.__serializer.to_format(data)
        with open(self.__file_path, "w", encoding="utf-8") as file:
            file.write(serialized_data)
        print(f"Данные успешно сохранены в файл: {self.__file_path}")

    def load_from_file(self) -> dict:
        with open(self.__file_path, "r", encoding="utf-8") as file:
            serialized_data = file.read()
        data = self.__serializer.from_format(serialized_data)
        users = []

        for user_data in data:
            if user_data['type'] not in USERS_FACTORY_MAP:
                raise TypeError
            user = USERS_FACTORY_MAP[user_data['type']](user_data['user_id'], user_data['name'], user_data['email'], user_data['age'])
            users.append(user)

        print(f"Данные успешно загружены из файла: {self.__file_path}")
        return users
    
    @property
    def file_path(self) -> str:
        return self.__file_path