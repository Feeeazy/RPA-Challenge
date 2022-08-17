from src.iniciar_challenge import iniciar_challenge
from src.navegador import driver
from src.var_fixas import *
from src.baixar_planilha import *

def main():

    iniciar_challenge(driver, URL_CHALLENGE)

    baixar_planilha(driver, URL_DOWNLOAD_SHEET)