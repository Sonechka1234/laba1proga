from abc import ABC, abstractmethod

class Serializer(ABC):
    @abstractmethod
    def to_format(self, movie: dict) -> str:
        pass
    
    @abstractmethod
    def from_format(self, data: dict) -> any:
        pass
    
    @abstractmethod
    def get_format(self) -> str:
        pass
