"""Connections handler"""


from socket import socket
from pickle import dumps
from threading import Thread
from user_handler import user_handler


def connections_handler(self) -> None:
    """Connections handler"""
    while True:
        try:
            user: socket = self.server_socket.accept()[0]

            # Sending encryption key
            request = ['CHIPER', self.chiper.key_str]
            user.send(dumps(request))

            # Getting user nikname
            # ['USER_NIKNAME', nikname]
            data: bytes = user.recv(9000)
            data = self.chiper.decrypt(data) # Decryption

            # If it's request for username
            if data[0] == 'USER_NIKNAME':
                # Check if the user's nickname is available
                if data[1].strip() and data[1].lower()\
                    not in self.busy_niknames and\
                    data[1].lower() != 'you' and not '\n' in data[1]\
                    and data[1].lower() != 'server':

                    # Add the user to the lists and
                    # send a connection notification to everyone
                    self.busy_niknames.append(data[1].lower())
                    self.users.append(user)
                    request = ['NEW_USER', data[1]]
                    self.send_to_all(request, user)

                    # Starting user handler
                    Thread(target=user_handler,
                        args=(self, user, data[1])
                        ).start()

                    print(f'New user: {data[1]}')
                    send_to_user = ['CONNECTION_STATUS', True]

                else:
                    send_to_user = ['CONNECTION_STATUS', False]

                # Sending information about connection to user
                send_to_user = self.chiper.encrypt(send_to_user) # Encryption
                user.send(send_to_user)

        # If an error occurs when connecting a user
        except Exception:
            pass
