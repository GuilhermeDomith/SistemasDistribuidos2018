from terminal import executarComando
import socket as s

sem_conexao = True
resposta = ''

def iniciarCliente():
	global sem_conexao

	socket = s.socket(s.AF_INET, s.SOCK_STREAM)
	socket.settimeout(20)

	while True:
		try:
			comando = ler_comando()
			if not comando:
				break

			conectar_com_servidor(socket)

			socket.send(comando.encode('utf-8'))
			resposta = receber_mensagem(socket)

			print(resposta)
		except KeyboardInterrupt:
			print("Programa interrompido.")
			break
		except:
			sem_conexao = True
			resposta = executarComando(comando)
			print(resposta)

	socket.close()
	print('Conexão encerrada')


def ler_comando():

	while True:
		comando = input('\ncomando: ')

		if not len(comando):
			continue
		elif comando.lower() == 'exit':
			return None
		else:
			return comando
		

def conectar_com_servidor(socket):
	global sem_conexao

	if sem_conexao:
		print("Sem conexão")
		socket.connect(('127.0.0.1', 25900))
		sem_conexao = False


def receber_mensagem(socket):
	tamanho = socket.recv(10).decode('utf-8')
	tamanho = float(tamanho)

	mensagem = ''
	quantRecebido = 0
	while quantRecebido < tamanho:
		recv = socket.recv(1024).decode('utf-8')

		quantRecebido += 1024
		mensagem += recv

	return mensagem


if __name__ == '__main__':
	iniciarCliente()