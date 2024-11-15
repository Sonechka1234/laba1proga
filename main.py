
from jsonSerializer import JsonSerializer
from storage import Storage
from user import UserVk
from xmlSerializer import XmlSerializer
from userService import UserService

if __name__ == "__main__":
    # jsonSerializer = JsonSerializer()
    xmlSerializer = XmlSerializer()
    storage = Storage(xmlSerializer)
    service = UserService(storage)
    user1 = service.create_user('UserTelegram', 48234, 'petya', 'ygf', 45)
    