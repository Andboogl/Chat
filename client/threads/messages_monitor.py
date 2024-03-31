"""Messages monitor thread"""


from PyQt6.QtCore import QThread, pyqtSignal
from connection import Connection


class MessagesMonitorThread(QThread):
    """Messages monitor thread"""
    signal = pyqtSignal(list)

    def __init__(self, connection_obj: Connection, main_window) -> None:
        super().__init__(None)
        self.connection_obj = connection_obj
        self.main_window = main_window
        self.running = True

    def run(self) -> None:
        """Run messages monitor"""
        while True:
            try:
                data = self.connection_obj.get_data_from_server()
                self.signal.emit([data])

            except Exception as error:
                self.signal.emit([str(error)])
                break
