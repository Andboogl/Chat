"""Server module"""


from socket import socket
from chiper import Chiper
from connections_handler import connections_handler


class Server:
    """Server"""
    def __init__(self, ip: str, port: int) -> None:
        """Initialization"""
        # Creation and setup of server socket
        self.server_socket = socket()
        self.server_socket.bind((ip, port))
        self.server_socket.listen(0)

        # Variables
        self.users = []
        self.busy_niknames = []
        self.chiper = Chiper()
        print('Server started working!')

        # Starting connections handler
        connections_handler(self)

    def send_to_all(self, request: list, do_not_send_to: socket = None) -> None:
        """Send some message to all users"""
        request = self.chiper.encrypt(request) # Encryption

        for user in self.users:
            try:
                # If it's not the specified user
                if user != do_not_send_to:
                    user.send(request)

            # If the user breaks the connection
            except Exception:
                continue
