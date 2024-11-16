
from jsonSerializer import JsonSerializer
from storage import Storage
from xmlSerializer import XmlSerializer
from userService import UserService

def main():

    try:
        print("Выбор формата файла: 1.json, 2.xml ")
        choice = input("Введите номер действия: ")
            
        if choice == "1":
            serializer = JsonSerializer()
            
        elif choice == "2":
            serializer = XmlSerializer()
            
        else:
            print("Неверный выбор, выход из программы.")
            return
        
        storage = Storage(serializer, "./db")
        service = UserService(storage)
        service.read_users()

        while True:
            print("\nВыберите действие:")
            print("1. Добавить пользователя")
            print("2. Обновить пользователя")
            print("3. Удалить пользователя")
            print("4. Показать всех пользователей")
            print("5. Выход")

            choice = input("Введите номер действия: ")

            try:
                if choice == "1":
                    user_type = input("Введите тип пользователя: ")
                    user_id = int(input("Введите ID пользователя: "))
                    name = input("Введите имя пользователя: ")
                    email = input("Введите email пользователя: ")
                    age = int(input("Введите возраст пользователя: "))
                    service.create_user(user_type, user_id, name, email, age)

                elif choice == "2":
                    user_id = int(input("Введите ID пользователя: "))
                    name = input("Введите новое имя пользователя: ")
                    email = input("Введите новый email пользователя: ")
                    age = int(input("Введите новый возраст пользователя: "))
                    service.update_user(user_id, name, email, age)

                elif choice == "3":
                    user_id = int(input("Введите ID пользователя: "))
                    service.delete_user(user_id)

                elif choice == "4":
                    service.read_users()

                elif choice == "5":
                    print("Выход из программы.")
                    break

                else:
                    print("Неверный выбор, попробуйте снова.")
            
            except TypeError:
                    print("Ошибка: Неизвестная соц сеть.")
            except Exception as e:
                print(f"Произошла непредвиденная ошибка: {e}")
    except KeyboardInterrupt:
        print("\nПрограмма завершена.")
    except Exception as e:
        print(f"Произошла ошибка: {e}")

if __name__ == "__main__":
    main()
   