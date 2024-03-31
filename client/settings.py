"""Settings module"""


from os import path, mkdir
from typing import Union
from json import load, dump


class Settings:
    """Settings class"""
    def __init__(self) -> None:
        # Settings file and folder path. You can change it
        self.settings_folder_path = path.join(path.expanduser('~'), 'Chat')
        self.settings_file_path = path.join(self.settings_folder_path, 'settings.json')

    def save_settings(self, data: dict) -> None:
        """Save settings to settings file"""
        # Creation of settings folder if it doesn't exists
        if not path.exists(self.settings_folder_path):
            mkdir(self.settings_folder_path)

        with open(self.settings_file_path,
                  'w', encoding='utf-8') as f:
            dump(data, f, indent=4)

    def get_settings(self) -> Union[dict, None]:
        """Get settings from settings file"""
        # If settings file is exists
        if path.exists(self.settings_file_path):
            with open(self.settings_file_path,
                    'r', encoding='utf-8') as f:
                return load(f)

