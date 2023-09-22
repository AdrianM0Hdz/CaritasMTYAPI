from typing import List
from uuid import uuid1
from hashlib import sha512


class Collector:
    def __init__(
        self,
        id: int,
        uuid: str,
        username: str,
        password: str,
        fullname: str,
        manager_id: str,
        tickets: List[str],
    ):
        assert isinstance(id, int)
        assert isinstance(uuid, str)
        assert isinstance(username, str)
        assert isinstance(password, str)
        assert isinstance(fullname, str)
        assert isinstance(manager_id, str)
        assert isinstance(tickets, list)

        self.id = id
        self.uuid = uuid
        self.username = username
        self.password = password
        self.fullname = fullname
        self.manager_id = manager_id
        self.tickets = tickets

    @classmethod
    def create_new(
        cls,
        uuid: str,
        username: str,
        password: str,
        fullname: str,
        manager_id: str,
    ):
        return cls(
            uuid=str(uuid1()),
            username=username,
            password=sha512(bytes(password, "utf-8")).hexdigest(),
            fullname=fullname,
            manager_id=manager_id,
            tickets=[],
        )
