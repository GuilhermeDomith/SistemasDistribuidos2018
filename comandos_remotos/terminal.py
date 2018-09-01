from subprocess import getoutput

def executarComando(comando):
    resultado_cmd = ''

    try:
        resultado_cmd = getoutput(comando)
    except Exception as e:
        print("Erro ao executar comando: " + str(e))
        resultado_cmd = str(e)

    return resultado_cmd
