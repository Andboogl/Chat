"""User handler"""


from socket import socket


def user_handler(self, user: socket, nikname: str) -> None:
    """User handler"""
    while True:
        try:
            data = user.recv(9000)
            data = self.chiper.decrypt(data) # Decryption

            # If it's request to exit
            # ['EXIT']
            if data[0] == 'EXIT':
                self.users.remove(user)
                self.busy_niknames.remove(nikname.lower())
                self.send_to_all(['EXIT', nikname, False])
                print(f'{nikname} exited')
                break

            # If it's request to a new message
            # ['MESSAGE', message]
            elif data[0] == 'MESSAGE':
                if data[1].strip():
                    request = ['MESSAGE', data[1], nikname]
                    self.send_to_all(request, user)
                    print(f'{nikname}: {data[1]}')

            # Deleting a user if they send
            # an unknown request, as it could
            # be a malicious user. You can delete it.
            else:
                self.users.remove(user)
                self.busy_niknames.remove(nikname.lower())
                self.send_to_all(['EXIT', nikname, True])
                print(f'{nikname} exited by an error')
                break

        # If the user logged out and
        # did not send the request or
        # failed to decrypt their request
        except Exception:
            self.users.remove(user)
            self.busy_niknames.remove(nikname.lower())
            self.send_to_all(['EXIT', nikname, True])
            print(f'{nikname} exited by an error')
            break
