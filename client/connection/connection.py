"""Connection module"""


from pickle import loads
from typing import Any
from socket import socket
from .chiper import Chiper


class InvalidNiknameError(Exception):
    """Error when nikname is invalid"""


class Connection:
    """Connection class"""
    def __init__(self,
                 ip: str,
                 port: int,
                 nikname: str) -> None:
        self.connection_socket = socket()
        self.connection_socket.connect((ip, port))
        self.connection_socket.settimeout(2)

        # Getting encryption key (chiper)
        # ['CHIPER', key]
        data = self.connection_socket.recv(9000)
        data = loads(data) # Decryption
        self.chiper = Chiper(data[1])

        # Sending user nikname to server
        request = ['USER_NIKNAME', nikname]
        self.send_request(request)

        # Getting connection status
        data = self.connection_socket.recv(9000)
        data = self.chiper.decrypt(data)

        if not data[1]:
            raise InvalidNiknameError('Incorrect nikname')

        self.connection_socket.settimeout(None)

    def send_request(self, request: list) -> None:
        """Send request to server"""
        request = self.chiper.encrypt(request) # Encryption
        self.connection_socket.send(request)

    def get_data_from_server(self) -> Any:
        """Get data from server"""
        data = self.connection_socket.recv(9000)
        data = self.chiper.decrypt(data) # Decryption
        return data
