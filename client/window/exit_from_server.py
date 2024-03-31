"""Exit from server"""


from .menus_block import block_or_unblock_chat, block_or_unblock_settings


def exit_from_server(self) -> None:
    """Exit from server"""
    try:
        # Sending request about exit and closing
        # connection socket and message monitor
        self.messages_monitor_thread.quit()
        self.connection.send_request(['EXIT'])
        self.connection.connection_socket.close()

    except Exception:
        pass

    # Unblocking settings and blocking chat
    block_or_unblock_chat(self, False)
    block_or_unblock_settings(self, True)
    self.design.chatbox.append('You exited')
