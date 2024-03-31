"""Main module. Runs server"""


from server import Server


def main() -> None:
    """This function runs server"""
    ip = input('Server IP: ')
    port = input('Server port: ')
    Server(ip, int(port))


if __name__ == '__main__':
    main()
