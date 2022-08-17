from selenium import webdriver
from src.var_fixas import *

class Abrir_Navegador():
    def __init__(self, driver_path, espera_implicita):
        self.driver = webdriver.Chrome(executable_path= driver_path)
        self.driver.implicitly_wait(espera_implicita)
        self.driver.maximize_window()
    def Abrir_Desafio(self):
        self.driver.get(URL_CHALLENGE)