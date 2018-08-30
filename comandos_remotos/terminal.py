from subprocess import getoutput

def executarComando(comando):
    resultado_cmd = ''

    try:
        resultado_cmd = getoutput(comando)
    except (FileNotFoundError, CalledProcessError) as e:
        resultado_cmd = 'Comando não encontrado.' + str(e)
    except Exception as e:
        resultado_cmd = str(e)

    return resultado_cmd
