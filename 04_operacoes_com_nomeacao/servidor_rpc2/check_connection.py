import socket as s

def check_connection_TCP(server_port):
    socket = s.socket(s.AF_INET, s.SOCK_STREAM)
    socket.bind(('', server_port))
    socket.listen(1)

    while True:
        try:
            connection, addr = socket.accept()
            connection.close()
        except KeyboardInterrupt:
            pass

    socket.close()