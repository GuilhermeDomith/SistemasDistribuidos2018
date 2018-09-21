#coding:utf-8
from cliente import montarEnviarOperacao

def soma(n1, n2):
    return montarEnviarOperacao({"op":"+", "n1": n1, "n2": n2})

def subtracao(n1, n2):
    return montarEnviarOperacao({"op":"-", "n1": n1, "n2": n2})

def multiplicacao(n1, n2):
    return montarEnviarOperacao({"op":"*", "n1": n1, "n2": n2})

def divisao(n1, n2):
    return montarEnviarOperacao({"op":"/", "n1": n1, "n2": n2})
