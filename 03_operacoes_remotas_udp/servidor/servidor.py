import hashlib
import json
import threading as thr
import socket as s

from modulo import operacoes
from check_connection import check_connection_TCP


UDP_PORT = 5005
TCP_PORT = 5004

def servidor_RCP():
    socket = s.socket(s.AF_INET, s.SOCK_DGRAM)
    socket.bind(('', UDP_PORT))

    while True:
        data, addr = socket.recvfrom(1024)
        data = json.loads(data.decode('utf-8'))

        resposta = operacoes[data['op']](data['n1'], data['n2'])
        print('mensagem: ', data)
        resposta = criar_hash(resposta) + '#' + str(resposta)
        socket.sendto(resposta.encode('utf-8'), addr)

    socket.close()

def criar_hash(mensagem):
    md5 = hashlib.md5()
    md5.update(str(mensagem).encode('utf-8'))
    return md5.hexdigest()

def main():
    thr.Thread( 
        target=check_connection_TCP, 
        args=(TCP_PORT, ), 
        name='Check Connection TCP', 
        daemon=True
    ).start()

    try: servidor_RCP()
    except KeyboardInterrupt: pass

if __name__ == '__main__':
    main()
