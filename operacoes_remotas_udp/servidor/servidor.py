import socket as s
import json
from modulo import *
import threading as thr
import hashlib

UDP_PORT = 5005
TCP_PORT = 5004

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
        data = json.loads(data.decode('utf-8'))

        resposta = operacoes[data['op']](data['n1'], data['n2'])
        print('mensagem: ', data)
        resposta = criar_hash(str(resposta)) + '#' + str(resposta)
        socket.sendto(resposta.encode('utf-8'), addr)

    socket.close()

def criar_hash(mensagem):
    md5 = hashlib.md5()
    md5.update(mensagem.encode('utf-8'))
    return md5.hexdigest()


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
