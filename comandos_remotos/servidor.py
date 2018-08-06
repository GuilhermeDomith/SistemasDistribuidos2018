import socket as s
import subprocess

def iniciar():
	socket = s.socket(s.AF_INET, s.SOCK_STREAM)
	socket.bind( ('localhost', 25000) )
	socket.listen(1)

	while True:
		try:
			print('Esperando conexão...')
			connection, addr = socket.accept()
			print('Conexão aceita.')
			atenderCliente(connection)
		except KeyboardInterrupt: break

	print('Servidor encerrado.')
	socket.close();


def atenderCliente(connection):

	while True:
		comando = connection.recv(1024).decode('utf-8')

		if comando.lower() == 'exit':
			break

		try:
			resultado_cmd = subprocess.check_output(comando.split(' '),
							universal_newlines=True,
							stderr=subprocess.STDOUT)
		except FileNotFoundError: resultado_cmd = 'Comando não encontrado.'
		except: break

		connection.send(resultado_cmd.encode('utf-8'))

	connection.close();
	print('Conexão encerrada')

if __name__ == '__main__':
	iniciar()
