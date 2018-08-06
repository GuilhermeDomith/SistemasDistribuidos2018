import socket as s
import servidor

socket = s.socket(s.AF_INET, s.SOCK_STREAM)
socket.connect( ('localhost', 25000) )

while True:
	try:
		comando = input('comando: ')
		if comando.lower() == 'exit':
			break;


			socket.send(comando.encode('utf-8'))
			resposta = socket.recv(1024)
			print(resposta.decode('utf-8'))
	except KeyboardInterrupt: break
	except: break

print('Conexão encerrada')
socket.close()
