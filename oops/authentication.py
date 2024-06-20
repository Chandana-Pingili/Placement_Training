from abc import ABC,abstractmethod


class Authentication(ABC):
    def __init__(self):
        self.__password="1234"
        self.username="Chandana"
    
    @abstractmethod
    def authenticate(self):
        pass

    def __get_password(self):
        return self.__password
    def access(self):
        return self.__get_password()