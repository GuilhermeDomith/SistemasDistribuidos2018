import socket as s
import servidor

socket = s.socket(s.AF_INET, s.SOCK_STREAM)
socket.connect(('localhost', 25000))

while True:
	try:
		comando = input('comando: ')
		if comando.lower() == 'exit':
			break

		socket.send(comando.encode('utf-8'))

		resposta = socket.recv(4096)
		print(resposta.decode('utf-8'))
	except KeyboardInterrupt as e:
		print(e)
		break
	except Exception as e:
		print(e)
		break

print('Conexão encerrada')
socket.close()
