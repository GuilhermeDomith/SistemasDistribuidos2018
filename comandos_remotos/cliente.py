from terminal import executarComando
import socket as s
import servidor

socket = s.socket(s.AF_INET, s.SOCK_STREAM)
socket.settimeout(2)
sem_conexao = True
resposta = ''

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
			socket.connect(('127.0.0.1', 25800))
			sem_conexao = False

		socket.send(comando.encode('utf-8'))
		tamanho = socket.recv(10).decode('utf-8')

		try:
			tamanho = int(tamanho)
		except:
			tamanho = 0

		# Receber resposta
		bufferResposta = ''
		tamanhoLido = 0
		while True:
			resposta = socket.recv(1024).decode('utf-8')
			tamanhoLido += 1024

			bufferResposta += resposta;
			tamanho += 1024

			if tamanhoLido >= tamanho:
				break


		print(bufferResposta)
	except KeyboardInterrupt:
		socket.close()
		break
	except (ConnectionRefusedError, OSError, s.timeout) as e:
		socket.close()
		sem_conexao = True
		resposta = executarComando(comando)
		print(resposta)

print('Conexão encerrada')
socket.close()
