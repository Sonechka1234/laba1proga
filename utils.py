from user import UserFacebook, UserIcq, UserInstagram, UserSnapchat, UserTumbler, UserTelegram, UserTwitter, UserViber, UserVk, UserWhatsApp

USERS_FACTORY_MAP = {
        'UserTelegram': lambda user_id, name, email, age: UserTelegram(user_id, name, email, age),
        'UserInstagram': lambda user_id, name, email, age: UserInstagram(user_id, name, email, age),
        'UserWhatsApp': lambda user_id, name, email, age: UserWhatsApp(user_id, name, email, age),
        'UserViber': lambda user_id, name, email, age: UserViber(user_id, name, email, age),
        'UserIcq':lambda user_id, name, email, age: UserIcq(user_id, name, email, age) ,
        'UserSnapchat': lambda user_id, name, email, age: UserSnapchat(user_id, name, email, age),
        'UserVk': lambda user_id, name, email, age: UserVk(user_id, name, email, age),
        'UserFacebook': lambda user_id, name, email, age: UserFacebook(user_id, name, email, age),
        'UserTwitter': lambda user_id, name, email, age: UserTwitter(user_id, name, email, age), 
        'UserTumbler':lambda user_id, name, email, age: UserTumbler(user_id, name, email, age)
    }