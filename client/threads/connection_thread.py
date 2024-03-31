"""Connection thread"""


from PyQt6.QtCore import QThread, pyqtSignal
from connection import Connection, InvalidNiknameError


class ConnectionThread(QThread):
    """Connection thread"""
    signal = pyqtSignal(list)

    def __init__(self,
                 ip: str,
                 port: int,
                 nikname: str) -> None:
        super().__init__(None)
        self.ip = ip
        self.port = port
        self.nikname = nikname

    def run(self) -> None:
        """Start connection"""
        try:
            connection = Connection(self.ip,
                                    self.port,
                                    self.nikname)

            self.signal.emit([connection])

        # If user nikname is unvalible
        except InvalidNiknameError:
            self.signal.emit(['Invalid nikname'])

        # If another error occurs
        except Exception as error:
            self.signal.emit([str(error)])
