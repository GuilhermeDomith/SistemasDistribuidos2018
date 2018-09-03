import socket as s
import json

def iniciarServidor():
    socket = s.socket(s.AF_INET, s.SOCK_STREAM)
    socket.bind(('', 25900))
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
        operacao = json.loads(mensagem)

        mensagem = ops[operacao['op']](operacao['n1'], operacao['n2'])

        connection.send(str(mensagem).encode('utf-8'))
        print(operacao)
    except Exception as e:
        print(e)

    connection.close()

def soma(a, b):
    return a + b

def subtracao(a, b):
    return a-b

def divisao(a, b):
    return a/b

def multiplicacao(a, b):
    return a*b

ops = {
    '+': soma,
    '-': subtracao,
    '/': divisao,
    '*': multiplicacao
}



if __name__ == '__main__':
    iniciarServidor()
