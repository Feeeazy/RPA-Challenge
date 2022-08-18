import os
from time import sleep

class Arquivo:
    def __init__(self, diretorio_download, diretorio_final):
        self.diretorio_download = diretorio_download
        self.diretorio_final = diretorio_final
    def mover(self):
        timer = 0
        timeout = 60

        arquivo_existe = os.path.exists(self.diretorio_download)
        timer_excedido = timer > timeout

        while not arquivo_existe:
            if timer_excedido:
                break
            sleep(1)
            timer = timer + 1
            arquivo_existe = os.path.exists(self.diretorio_download)
            timer_excedido = timer > timeout
        
        if arquivo_existe:
            os.replace(self.diretorio_download, self.diretorio_final)
        else:
            raise Exception("Não foi realizado o download do arquivo.")

def teste_existencia(diretorio_final):
    if os.path.exists(diretorio_final):
        return True