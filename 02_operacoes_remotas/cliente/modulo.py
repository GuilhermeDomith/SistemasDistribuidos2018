from cliente_rpc import enviar_operacao

def soma(a, b):
    return enviar_operacao({'op':'+', 'n1': a, 'n2': b})

def subtracao(a, b):
    return enviar_operacao({'op':'-', 'n1': a, 'n2': b})

def divisao(a, b):
    return enviar_operacao({'op':'/', 'n1': a, 'n2': b})

def multiplicacao(a, b):
    return enviar_operacao({'op':'*', 'n1': a, 'n2': b})
