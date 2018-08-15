from subprocess import check_output, STDOUT, CalledProcessError

def executarComando(comando):
    try:

        resultado_cmd = check_output(comando,
                                     universal_newlines=True,
                                     shell=True,
                                     stderr=STDOUT)
        if not resultado_cmd:
            resultado_cmd = 'O comando não pôde ser executado.'

    except (FileNotFoundError, CalledProcessError):
        resultado_cmd = 'Comando não encontrado.'
        
    return resultado_cmd
