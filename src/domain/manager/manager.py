from typing import List
from hashlib import sha512
from uuid import uuid1

from ..ticket import Ticket 
from ..collector import Collector

class Manager:
    def __init__(
        self,
        id: int,
        uuid: str,
        username: str,
        password: str,
        fullname: str,
        collectors: List[Collector],
        tickets: List[Ticket],
    ):
        assert isinstance(id, int)
        assert isinstance(uuid, str)
        assert isinstance(username, str)
        assert isinstance(password, str)
        assert isinstance(fullname, str)
        assert isinstance(collectors, list)
        assert isinstance(tickets, list)

        self.__id = id
        self.__uuid = uuid
        self.__username = username
        self.__password = password
        self.__fullname = fullname
        self.__collectors = collectors
        self.__tickets = tickets

    @property
    def id(self) -> int:
        return self.__id

    @property
    def uuid(self) -> str:
        return self.__uuid

    @property
    def username(self) -> str:
        return self.__username

    @property
    def password(self) -> str:
        return self.__password

    @property 
    def fullname(self) -> str:
        return self.__fullname
    
    @property 
    def collectors(self) -> List[Collector]:
        return self.__collectors 

    @property 
    def tickets(self) -> List[Ticket]:
        return self.__tickets

    @classmethod
    def create_new(cls, username: str, password: str, fullname: str):
        return cls(
            uuid=str(uuid1()),
            username=username,
            password=sha512(bytes(password, "utf-8")).hexdigest(),
            fullname=fullname,
            collectors=[],
            tickets=[],
        )
