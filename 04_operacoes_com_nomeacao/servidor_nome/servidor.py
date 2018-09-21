import json
import socket as s


UDP_PORT = 8888

def servidor_nomes(socket):

    while True:
        data, addr = socket.recvfrom(1024)
        print('Conectado com o host {}'.format(addr))
        data = data.decode('utf-8')

        with open('operacoes_ips.json') as file:
            nomes = json.load(file)

            servidor = "Operação inválida"
            if data in nomes:
                servidor = json.dumps(nomes[data])

            socket.sendto(servidor.encode('utf-8'), addr)

def main():
    socket = s.socket(s.AF_INET, s.SOCK_DGRAM)
    socket.bind(('', UDP_PORT))
    try: 
        servidor_nomes(socket)
    except KeyboardInterrupt: 
        socket.close()

if __name__ == '__main__':
    main()
