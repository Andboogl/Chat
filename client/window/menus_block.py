"""Module to block menus widgets"""


def block_or_unblock_settings(self, block: bool) -> None:
    """Block or unblock settings menu widgets"""
    self.design.nikname.setEnabled(block)
    self.design.server_ip.setEnabled(block)
    self.design.server_port.setEnabled(block)
    self.design.connect.setEnabled(block)
    self.design.save_settings.setEnabled(block)

def block_or_unblock_chat(self, block: bool) -> None:
    """Block or unblock chat menu widgets"""
    self.design.user_message.setEnabled(block)
    self.design.send_message.setEnabled(block)
    self.design.exit.setEnabled(block)
