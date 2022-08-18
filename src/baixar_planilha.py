from src.mover_arquivo import Arquivo
from src.mover_arquivo import teste_existencia
from src.var_fixas import *

def baixar_planilha(driver, url_download):
    if teste_existencia(DIRETORIO_CHALLENGE):
        return print('O arquivo excel do RPA Challenge já existe no diretório /bin.')
    else:
        driver.get(url_download)
        Arquivo(DIRETORIO_DOWNLOAD, DIRETORIO_CHALLENGE).mover()