import json
from serializer import Serializer


class JsonSerializer(Serializer):
    def to_format(self, users: dict) -> str:
        return json.dumps(users, indent=4)
    
  
    def from_format(self, data: dict) -> any:
        return json.loads(data)
   