import json
from serializer import Serializer


class JsonSerializer(Serializer):
    def to_format(self, users: dict) -> str:
        users_data = [{"type": user.__class__.__name__, "name": user.name, "age": user.age} for user in users]
        return json.dumps(users_data, indent=4)
    
  
    def from_format(self, data: dict) -> any:
        return json.loads(data)
   