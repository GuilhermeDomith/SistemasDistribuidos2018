import socket as s
import json
from modulo import *
import threading as thr

UDP_PORT = 5005
TCP_PORT = 5006

def main():
    thr.Thread(target=check_connection_TCP, args=(), name='Conexão Server TCP', daemon=True).start()
    try:
        servidor_RCP()
    except KeyboardInterrupt:
        pass

def servidor_RCP():
    socket = s.socket(s.AF_INET, s.SOCK_DGRAM)
    socket.bind(('', UDP_PORT))

    while True:
        data, addr = socket.recvfrom(1024)
        print('operacao:  ', addr)
        data = json.loads(data.decode('utf-8'))

        resposta = operacoes[data['op']](data['n1'], data['n2'])
        print('resposta: ', resposta)
        socket.sendto(str(resposta).encode('utf-8'), addr)

    socket.close()


def check_connection_TCP():
    socket = s.socket(s.AF_INET, s.SOCK_STREAM)
    socket.bind(('', TCP_PORT))
    socket.listen(1)

    while True:
        try:
            connection, addr = socket.accept()
            connection.close()
        except KeyboardInterrupt:
            pass

    socket.close()

if __name__ == '__main__':
    main()
