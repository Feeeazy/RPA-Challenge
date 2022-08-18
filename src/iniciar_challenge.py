from src.var_fixas import *
from selenium.webdriver.common.by import By
from .ler_excel import ArquivoChallenge

class Challenge:
    def __init__(self):
        pass
    def iniciar(self, driver, url):
        self.driver = driver
        self.url = url
        self.driver.get(self.url)
        self.driver.find_element(By.XPATH, '(/html/body/app-root/div[2]/app-rpa1/div/div[1]/div[6]/button)[1]').click()

def submit(driver):
    driver.find_element(By.XPATH, '(//input[@type= "submit"])[1]').click()

def preencher_input(driver, label_name, input):
    print(f'Entrou no preencher_input com os seguintes dados {label_name} e {input}')
    driver.find_element(By.XPATH, f'//input[@ng-reflect-name= "{label_name}"]').send_keys(input)

def input_dados(driver):
    dados = ArquivoChallenge(DIRETORIO_CHALLENGE).ler_arquivo()
    linha = 0
    while linha < len(dados.index):
        d = dados.iloc[linha]

        firt_name       = d[0]
        last_name       = d[1]
        company_name    = d[2]
        role_in_company = d[3]
        address         = d[4]
        email           = d[5]
        phone_number    = str(d[6])

        preencher_input(driver, 'labelFirstName', firt_name)
        preencher_input(driver, 'labelLastName', last_name)
        preencher_input(driver, 'labelCompanyName', company_name)
        preencher_input(driver, 'labelRole', role_in_company)
        preencher_input(driver, 'labelAddress', address)
        preencher_input(driver, 'labelEmail', email)
        preencher_input(driver, 'labelPhone', phone_number)

        linha = linha + 1

        submit(driver)


