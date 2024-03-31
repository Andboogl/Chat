"""Application main window module"""


from PyQt6.QtWidgets import QMainWindow
from design.design import Ui_MainWindow
from settings import Settings
from .connection_with_server import connect_to_server, send_message
from .exit_from_server import exit_from_server
from .settings import save_settings, get_settings
from .menus_block import block_or_unblock_chat


class MainWindow(QMainWindow):
    """Application main window"""
    def __init__(self, parent: None = None) -> None:
        super().__init__(parent)

        # Loading design
        self.design = Ui_MainWindow()
        self.design.setupUi(self)

        # Initialization
        self.settings = Settings()
        block_or_unblock_chat(self, False)
        get_settings(self)

        # Button pressing
        self.design.save_settings.clicked.connect(
            lambda: save_settings(self))
        self.design.go_to_chat.clicked.connect(
            lambda: self.design.tabWidget.setCurrentIndex(0))
        self.design.connect.clicked.connect(
            lambda: connect_to_server(self))
        self.design.exit.clicked.connect(
            lambda: exit_from_server(self))
        self.design.send_message.clicked.connect(
            lambda: send_message(self))

    def closeEvent(self, a0) -> None:
        """When user close application"""
        exit_from_server(self)
        a0.accept()
