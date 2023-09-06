from typing import List
from hashlib import sha512
from uuid import uuid1


class Manager:
    def __init__(
        self,
        id: str,
        username: str,
        password: str,
        fullname: str,
        collectors: List[str],
        tickets: List[str],
    ):
        assert isinstance(id, str)
        assert isinstance(username, str)
        assert isinstance(password, str)
        assert isinstance(fullname, str)
        assert isinstance(collectors, list)
        assert isinstance(tickets, list)

        self.__id = id
        self.__username = username
        self.__password = password
        self.fullname = fullname
        self.collectors = collectors
        self.tickets = tickets

    @property
    def id(self) -> str:
        return self.__id

    @property
    def username(self) -> str:
        return self.__username

    @property
    def password(self) -> str:
        return self.__password

    @classmethod
    def create_new(cls, username: str, password: str, fullname: str):
        return cls(
            id=str(uuid1()),
            username=username,
            password=sha512(bytes(password, "utf-8")).hexdigest(),
            fullname=fullname,
            collectors=[],
            tickets=[],
        )
