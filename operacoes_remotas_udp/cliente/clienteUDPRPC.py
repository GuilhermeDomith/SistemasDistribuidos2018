#coding:utf-8

import socket as skt
import json
import hashlib

PORTA = 5005

servidor = '10.3.1.21'


def soma(n1, n2):
    return montarEnviarOperacao({"op":"+", "n1": n1, "n2": n2})

def subtracao(n1, n2):
    return montarEnviarOperacao({"op":"-", "n1": n1, "n2": n2})

def multiplicacao(n1, n2):
    return montarEnviarOperacao({"op":"*", "n1": n1, "n2": n2})

def divisao(n1, n2):
    return montarEnviarOperacao({"op":"/", "n1": n1, "n2": n2})

def montarEnviarOperacao(operacaoEmJSON):
    nTry = 6
    while nTry > 0:
        if checkComputer(servidor):
            socket = skt.socket(skt.AF_INET, skt.SOCK_DGRAM)
            socket.settimeout(5)

            data = None

            try:
                socket.sendto(json.dumps(operacaoEmJSON).encode('utf-8'), (servidor, PORTA))
                data, addr = socket.recvfrom(1024)

            except skt.timeout:
                nTry-=1
                print('O servidor não respondeu a solicitação! Será feita uma nova tentativa...')
                continue

            strQuebrada = None

            try:
                strQuebrada = data.partition('#')

                if strQuebrada[0] == str(gerar_hash(strQuebrada[2])):
                    return strQuebrada[2]
                else:
                    print('A resposta recebida não é íntegra! Será realizada uma nova tentativa...')
                    nTry-=1
                    continue
            except Exception:
                print('A resposta recebida não é íntegra! Será realizada uma nova tentativa...')
                nTry-=1
                continue
        else:
            print('Servidor Inativo!')
            nTry-=1
            print('Tentando conectar novamente....')

    return 'Ocorreu um erro durante a execução do programa!Contate a equipe de TI...'


def gerar_hash(dados):
    md5 = hashlib.md5()
    md5.update(dados.encode('utf-8'))
    return md5.hexdigest()


'''
Checa se o computador esta ativo
'''
def checkComputer(ip_address):
    try:
        s = skt.socket(skt.AF_INET, skt.SOCK_STREAM)
        s.settimeout(1.5)
        s.connect((ip_address, 5004))
        s.close()
        return True
    except skt.error:
        return False
