import json
from serializer import Serializer


class JsonSerializer(Serializer):
    def to_format(self, users: dict) -> str:
        users_data = [{"type": user.__class__.__name__, "user_id": user.user_id, "name": user.name, "email": user.email, "age": user.age} for user in users]
        return json.dumps(users_data, indent=4)
  
    def from_format(self, data: dict) -> any:
        return json.loads(data)
    
    def get_format(self):
        return 'json'
   
   