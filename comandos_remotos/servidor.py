import socket as s
from terminal import executarComando


def iniciarServidor():
    socket = s.socket(s.AF_INET, s.SOCK_STREAM)
    socket.bind(('', 25900))
    socket.listen(1)

    while True:
        try:
            print('Esperando conexão...')
            connection, addr = socket.accept()
            print('Conexão aceita.')

            connection.settimeout(10)
            atenderCliente(connection)
        except KeyboardInterrupt:
            break

    print('Servidor encerrado.')
    socket.close()


def atenderCliente(connection):

    while True:
        try:
            comando = connection.recv(1024).decode('utf-8')
            if comando.lower() == 'exit':
                break

            resultado_cmd = executarComando(comando) + '\n server'
            tamanhoResposta = str(len(resultado_cmd)).zfill(10)
            resultado_cmd = tamanhoResposta + resultado_cmd

            print(resultado_cmd)
            connection.send(resultado_cmd.encode('utf-8'))
        except Exception as e:
            print(e)
            break

    connection.close()
    print('Conexão encerrada')


if __name__ == '__main__':
    iniciarServidor()
