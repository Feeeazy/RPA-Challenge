from webbrowser import Chrome
from src.abrir_navegador import *

def Main():
    teste1 = Abrir_Navegador(driver_path= CHROME_DRIVER_PATH, espera_implicita= IMPLICITY_WAIT)
    teste1.Abrir_Desafio()