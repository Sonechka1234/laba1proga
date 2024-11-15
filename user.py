class User:
    def __init__(self, user_id: int, name: str, email: str, age: int):
        self.__user_id = user_id
        self.__name = name
        self.__email = email
        self.__age = age

    @property
    def user_id(self):
        return self.__user_id
    
    @user_id.setter
    def user_id(self, user_id: int):
        self.__user_id = user_id

    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, name: str):
        self.name = name

    @property
    def email(self):
        return self.__email
    
    @email.setter
    def email(self, email: str):
        self.__email = email

    @property
    def age(self):
        return self.__age
    
    @age.setter
    def age(self, age: int):
        self.__age = age
    
    def get_info(self):
        pass

class UserTelegram(User):
    def get_info(self):
        return 'Это пользователь телеграм'

class UserInstagram(User):
    def get_info(self):
        return 'Это пользователь инстаграм' 

class UserWhatsApp(User):
    def get_info(self):
        return 'Это пользователь Ватсапп'

class UserViber(User):
    def get_info(self):
        return 'Это пользователь вайбер'

class UserIcq(User):
    def get_info(self):
        return 'Это пользователь аськи'

class UserSnapchat(User):
    def get_info(self):
        return 'Это пользователь снапчат'

class UserVk(User):
    def get_info(self):
        return 'Это пользователь вк'
    
class UserFacebook(User):
    def get_info(self):
        return 'Это пользователь фейсбук'
    
class UserTwitter(User):
    def get_info(self):
        return 'Это пользователь твиттер'
    
class UserTumbler(User):
    def get_info(self):
        return 'Это пользователь тамблер'


