from selenium import webdriver
from selenium.webdriver.common.by import By
from src.var_fixas import *

def Abrir_Navegador(driver_path, espera_implicita):
    driver = webdriver.Chrome(executable_path= driver_path)
    driver.implicitly_wait(espera_implicita)
    driver.maximize_window()