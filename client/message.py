"""Module to show message"""


from PyQt6.QtWidgets import QMessageBox


def show_message(text: str) -> None:
    """Show message on the screen use QMessageBox"""
    msg_box = QMessageBox()
    msg_box.setText(text)
    msg_box.exec()
