"""Connection to server module"""


from threads import ConnectionThread
from message import show_message
from .settings import check_settings_data
from .signals_handlers import connection_signals_handlers


def connect_to_server(self) -> None:
    """Connect to server"""
    if check_settings_data(self):
        nikname = self.design.nikname.text()
        server_ip = self.design.server_ip.text()
        server_port = int(self.design.server_port.text())

        # Starting connection thread
        self.connection_thread = ConnectionThread(server_ip,
                                             server_port,
                                             nikname)
        self.connection_thread.signal.connect(
            lambda value: connection_signals_handlers(self, value))
        self.connection_thread.start()

def send_message(self) -> None:
    """Send message"""
    message = self.design.user_message.text()

    if message.strip():
        try:
            self.connection.send_request(['MESSAGE', message])
            self.design.chatbox.append(f'You: {message}')

        except Exception as error:
            exit_from_server()
            show_message('Error while '\
                         'sending messa'\
                         'ge. Maybe ser'\
                         'ver is unvalibl'\
                         f'e. {error}')

    else:
        show_message('You can\'t send empty message')
