"""Connection to server signals handlers"""


from typing import Union
from connection import Connection
from message import show_message
from threads import MessagesMonitorThread
from ..menus_block import block_or_unblock_chat, block_or_unblock_settings
from .messages_monitor_signals_handlers import messages_monitor_signals_handlers


def connection_signals_handlers(self, value: Union[str, Connection]) -> None:
    """Signals handlers for connection to server thread"""
    value = value[0]

    # If the connection was successful
    if isinstance(value, Connection):
        self.connection = value

        # Starting of messages monitor
        self.messages_monitor_thread = MessagesMonitorThread(self.connection,
                                                                self)
        self.messages_monitor_thread.signal.connect(
            lambda value: messages_monitor_signals_handlers(self, value))
        self.messages_monitor_thread.start()

        block_or_unblock_settings(self, False)
        block_or_unblock_chat(self, True)
        self.design.chatbox.clear()
        self.design.chatbox.append('You connected to server!')

    # If the user's nickname is not available
    elif value == 'Invalid nikname':
        show_message('This nikname is busy or incorrect')

    # If another error occurs when connecting to the server
    else:
        show_message('Error when connecting '\
                        'to the server. Check the '\
                        'IP and port. Maybe this '\
                        'server does not support '\
                        'this chat')

    self.connection_thread.quit()
