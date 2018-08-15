from terminal import executarComando
import socket as s
import servidor

socket = s.socket(s.AF_INET, s.SOCK_STREAM)
socket.settimeout(2)
sem_conexao = True

while True:
	try:
		comando = input('comando: ')
		if comando.lower() == 'exit':
			break
		elif not len(comando):
			continue
		
		# Se não houver conexão irá conectar com o servidor, se
		# o mesmo estiver insdisponível irá disparar ConnectionRefusedError.
		if sem_conexao:
			socket.connect(('127.0.0.1', 25000))
			sem_conexao = False

		socket.send(comando.encode('utf-8'))
		resposta = socket.recv(4096).decode('utf-8')

		# Verifica se houve resposta, se ocorreu timeout.
		if len(resposta) == 0:
			raise s.timeout
	except KeyboardInterrupt:
		break
	except (ConnectionRefusedError, OSError, s.timeout) as e:
		sem_conexao = True
		resposta = executarComando(comando)
	
	print(resposta)

print('Conexão encerrada')
socket.close()
