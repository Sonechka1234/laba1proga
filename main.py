
from jsonSerializer import JsonSerializer
from storage import Storage
from user import UserVk
from xmlSerializer import XmlSerializer
from userService import UserService

def main():
    serializer = XmlSerializer()
    storage = Storage(serializer)
    service = UserService(storage)

    while True:
        print("\nВыберите действие:")
        print("1. Добавить пользователя")
        print("2. Обновить пользователя")
        print("3. Удалить пользователя")
        print("4. Показать всех пользователей")
        print("5. Выход")

        choice = input("Введите номер действия: ")

        if choice == "1":
            user_type = input("Введите тип пользователя: ")
            user_id = int(input("Введите ID пользователя: "))
            name = input("Введите имя пользователя: ")
            email = input("Введите email пользователя: ")
            age = int(input("Введите возраст пользователя: "))
            service.create_user(user_type, user_id, name, email, age)

        elif choice == "2":
            user_type = input("Введите тип пользователя: ")
            user_id = int(input("Введите ID пользователя: "))
            name = input("Введите новое имя пользователя: ")
            email = input("Введите новый email пользователя: ")
            age = int(input("Введите новый возраст пользователя: "))
            service.update_user(user_type, user_id, name, email, age)

        elif choice == "3":
            user_type = input("Введите тип пользователя: ")
            user_id = int(input("Введите ID пользователя: "))
            service.delete_user(user_type, user_id)

        elif choice == "4":
            service.read_users()

        elif choice == "5":
            print("Выход из программы.")
            break

        else:
            print("Неверный выбор, попробуйте снова.")

if __name__ == "__main__":
    main()
   