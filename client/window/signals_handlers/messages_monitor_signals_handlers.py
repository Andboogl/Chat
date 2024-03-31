"""Messages monitor signals handlers"""


from message import show_message
from ..exit_from_server import exit_from_server


def messages_monitor_signals_handlers(self, value) -> None:
    """Messages monitor signals handlers"""
    value = value[0]

    # If it's message from server
    if isinstance(value, list):
        # If it's request for a new message
        # ['MESSAGE', message, nikname]
        if value[0] == 'MESSAGE':
            message = f'{value[2]}: {value[1]}'
            self.design.chatbox.append(message)

        # If it's request for a new user
        # ['NEW_USER', nikname]
        elif value[0] == 'NEW_USER':
            message = f'{value[1]} connected'
            self.design.chatbox.append(message)

        # If it's request for a user exit
        # ['EXIT', nikname]
        elif value[0] == 'EXIT':
            message = f'{value[1]} exited by an error' if \
                    value[2] else f'{value[1]} exited'
            self.design.chatbox.append(message)

    # If it's error with connection
    elif isinstance(value, str):
        if self.messages_monitor_thread.isRunning():
            exit_from_server(self)
            show_message('Error while receiving data from '\
                         'the server. Check if you are con'\
                         f'nected to the correct server. {value}')
            self.messages_monitor_thread.quit()

