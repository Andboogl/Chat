"""Chiper"""


from pickle import loads, dumps
from typing import Any
from cryptography.fernet import Fernet


class Chiper:
    """Chiper"""
    def __init__(self) -> None:
        self.key_str: str = Fernet.generate_key()
        self.chiper = Fernet(self.key_str)

    def encrypt(self, data: Any) -> bytes:
        """Encrypt data"""
        result: bytes = self.chiper.encrypt(dumps(data))
        return result

    def decrypt(self, data: bytes) -> Any:
        """Decrypt data"""
        result: Any = loads(self.chiper.decrypt(data))
        return result
