from selenium import webdriver
from src.var_fixas import *

class Navegador:
    def __init__(self, driver_path, espera_implicita, maximizar = MAXIMIZAR):
        self.driver_path = driver_path
        self.espera_implicita = espera_implicita
        self.maximizar = maximizar
    def start(self):
        self.driver = webdriver.Chrome(executable_path= self.driver_path)
        self.driver.implicitly_wait(self.espera_implicita)
        if self.maximizar:
            self.driver.maximize_window()
        return self.driver

driver = Navegador(driver_path=CHROME_DRIVER_PATH, espera_implicita=IMPLICITY_WAIT).start()