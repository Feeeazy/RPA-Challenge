from src.mover_arquivo import Mover_Arquivo
from src.var_fixas import *

def baixar_planilha(driver, url_download):

    driver.get(url_download)

    Mover_Arquivo()