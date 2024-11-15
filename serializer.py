from abc import ABC, abstractmethod

class Serializer(ABC):
    @abstractmethod
    def to_format(self, users: dict):
        pass
    @abstractmethod   
    def from_format(self, data: dict):
        pass
    