from .iniciar_challenge import *
from .navegador import driver
from .var_fixas import *
from .baixar_planilha import *

def main():

    baixar_planilha(driver, URL_DOWNLOAD_SHEET)

    Challenge().iniciar(driver, URL_CHALLENGE)

    input_dados(driver)