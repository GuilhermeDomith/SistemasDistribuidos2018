from cliente_rpc import enviar_operacao

def soma(a, b):
    return enviar_operacao({'soma':[a,b]})

def subtracao(a, b):
    return a-b

def divisao(a, b):
    return a/b
