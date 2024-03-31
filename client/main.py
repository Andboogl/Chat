"""Main module. Runs application"""


from sys import argv
from PyQt6.QtWidgets import QApplication
from window import MainWindow


def main() -> None:
    """This function runs application"""
    app = QApplication(argv)
    window = MainWindow()
    window.show()
    app.exec()


if __name__ == '__main__':
    main()
