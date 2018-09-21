import socket as skt
import json
import hashlib

PORTA = 8888
servidorDNS = '10.3.1.19'


def montarEnviarOperacao(operacaoEmJSON):
    servidores = consultarDNS(operacaoEmJSON["op"])

    if servidores == None:
        print('Servidor DNS não está disponível!')
        return

    operacao = '%d %s %d'%(operacaoEmJSON['n1'], operacaoEmJSON['op'], operacaoEmJSON['n2'])
    for servidor in servidores:
        if checkComputer(servidor):
            try: 
                resposta = enviarRequisicao(servidor["ip"], servidor["porta"], operacaoEmJSON)
                return operacao +': '+resposta
            except: 
                continue
            
    return "%s: Não pode ser resolvida."%operacao


def consultarDNS(operacao):
    socket = skt.socket(skt.AF_INET, skt.SOCK_DGRAM)
    socket.settimeout(5)

    try:
        socket.sendto(operacao.encode('utf-8'), (servidorDNS, PORTA))
        data, addr = socket.recvfrom(1024)

        jsonResponse = json.loads(data.decode('utf-8'))

        return jsonResponse

    except skt.timeout:
        return None



def enviarRequisicao(ser, pt, operacaoEmJSON):
    # Cria o socket e define o timeout
    socket = skt.socket(skt.AF_INET, skt.SOCK_DGRAM)
    socket.settimeout(5)

    data = None

    # Envia a requisição e aguarda pela resposta do servidor
    socket.sendto(json.dumps(operacaoEmJSON).encode('utf-8'), (ser, pt))
    data, addr = socket.recvfrom(1024)    
    strQuebrada = data.decode('utf-8').rpartition('#')

    if strQuebrada[0] == str(gerar_hash(strQuebrada[2])):
        return strQuebrada[2]
    
    raise Exception



def gerar_hash(dados):
    md5 = hashlib.md5()
    md5.update(dados.encode('utf-8'))
    return md5.hexdigest()


'''
Checa se o computador esta ativo
'''
def checkComputer(servidor):
    try:
        s = skt.socket(skt.AF_INET, skt.SOCK_STREAM)
        s.settimeout(1.5)
        s.connect((servidor["ip"], servidor["portaTCP"]))
        s.close()
        return True
    except skt.error:
        return False