"""The module provides work with settings in the interface"""


from os import remove
from message import show_message


def get_settings(self) -> None:
    """Get settings and load it in GUI"""
    try:
        settings = self.settings.get_settings()

        # If settings exists
        if settings:
            self.design.nikname.setText(settings['nikname'])
            self.design.server_ip.setText(settings['server_ip'])
            self.design.server_port.setText(settings['server_port'])

    # If an error occurs while loading settings
    except Exception as error:
        show_message(f'Error while loading user settings: {error}')
        remove(self.settings.settings_file_path)

def check_settings_data(self) -> None:
    """Check settings data"""
    # Getting user settings from LineEdits
    nikname = self.design.nikname.text()
    server_ip = self.design.server_ip.text()
    server_port = self.design.server_port.text()

    # If all definitions are not empty
    if nikname.strip() and server_ip.strip() and server_port.strip():
        # If server port is a number
        if server_port.isdecimal():
            return (nikname, server_ip, server_port)

        else:
            show_message('Port must have only numbers')

    else:
        show_message('Enter all data')

def save_settings(self) -> None:
    """Save user settings"""
    if check_settings_data(self):
        settings = {'nikname': self.design.nikname.text(),
                'server_ip': self.design.server_ip.text(),
                'server_port': self.design.server_port.text()}
        self.settings.save_settings(settings)
