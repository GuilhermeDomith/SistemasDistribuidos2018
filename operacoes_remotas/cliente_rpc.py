import socket as s
import json

def enviar_operacao(operacao):
    socket = s.socket(s.AF_INET, s.SOCK_STREAM)
    socket.settimeout(20)

    try:
        socket.connect(('127.0.0.1', 25600))

        socket.send(json.dumps(operacao).encode('utf-8'))
        resposta = socket.recv(1024).decode('utf-8')

        print(resposta)
    except KeyboardInterrupt:
        print("Programa interrompido.")

    socket.close()
    print('Conexão encerrada')
    return resposta
