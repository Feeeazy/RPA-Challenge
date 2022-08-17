from selenium import webdriver
from src.var_fixas import *

def Iniciar_Challenge(driver, url):
    driver.get(url)