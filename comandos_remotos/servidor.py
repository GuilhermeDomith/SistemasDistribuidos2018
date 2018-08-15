import socket as s
from terminal import executarComando


def iniciarServidor():
    socket = s.socket(s.AF_INET, s.SOCK_STREAM)
    socket.bind(('', 25000))
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
            comando = connection.recv(2048).decode('utf-8')
            if comando.lower() == 'exit':
                break

            resultado_cmd = executarComando(comando) + "\nserver"
            connection.send(resultado_cmd.encode('utf-8'))
        except:
            break

    connection.close()
    print('Conexão encerrada')


if __name__ == '__main__':
    iniciarServidor()
