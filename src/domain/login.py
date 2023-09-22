from typing import Union
from hashlib import sha512

from .collector import Collector
from .manager import Manager

def is_user_password(item: Union[Collector, Manager], password: str) -> bool:
    """Checks if the password is equal to the password of item"""
    hashed_password = sha512(bytes(password, "utf-8")).hexdigest()
    return hashed_password == item.password
