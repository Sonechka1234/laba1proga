from serializer import Serializer

class Storage:
    def __init__(self, serializer: Serializer):
        self.__serializer = serializer

    def save_to_file(self, data: dict, file_path: str) -> None:
        serialized_data = self.__serializer.to_format(data)
        with open(file_path, "w", encoding="utf-8") as file:
            file.write(serialized_data)
        print(f"Данные успешно сохранены в файл: {file_path}")

    def load_from_file(self, file_path: str) -> dict:
        with open(file_path, "r", encoding="utf-8") as file:
            serialized_data = file.read()
        data = self.__serializer.from_format(serialized_data)
        print(f"Данные успешно загружены из файла: {file_path}")
        return data