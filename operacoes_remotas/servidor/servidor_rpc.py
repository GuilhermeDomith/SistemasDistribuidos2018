import socket as s
from modulo import *
import json

def iniciarServidor():
    socket = s.socket(s.AF_INET, s.SOCK_STREAM)
    socket.bind(('', 25600))
    socket.listen(1)

    while True:
        try:
            print('Esperando conexão...')
            connection, addr = socket.accept()
            print('Conexão aceita.')

            connection.settimeout(20)
            atenderCliente(connection)
        except KeyboardInterrupt:
            print("Programa interrompido.")
            break

    print('Servidor encerrado.')
    socket.close()


def atenderCliente(connection):
    try:
        mensagem = connection.recv(1024).decode('utf-8')
        mensagem = json.loads(mensagem)

        operacao = mensagem['op']
        mensagem = operacoes[operacao](mensagem['n1'], mensagem['n2'])

        connection.send(str(mensagem).encode('utf-8'))
        print(operacao)
    except Exception as e:
        print(e)

    connection.close()


if __name__ == '__main__':
    iniciarServidor()
