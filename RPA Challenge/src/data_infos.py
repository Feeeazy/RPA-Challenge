import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By


class Main:
    def __init__(self, file_xlsx):
        print('__init__ - Start')
        self.file_xlsx = file_xlsx
        self.open_browser()
        print('__init__ - End')
    
    def read_file(self):
        print('read_file - Start')
        self.file_xlsx = pd.read_excel(self.file_xlsx)
        print('read_file - End')
    
    def list_infos(self, line_number):
        print('get_info - Start')
        data_line = pd.DataFrame(self.file_xlsx)
        first_name = data_line.iloc[line_number, 0]
        last_name = data_line.iloc[line_number, 1]
        company_name = data_line.iloc[line_number, 2]
        role_in_company = data_line.iloc[line_number, 3]
        address = data_line.iloc[line_number, 4]
        email = data_line.iloc[line_number, 5]
        phone_number = str(data_line.iloc[line_number, 6])
        print('get_info - End')
        return [first_name, last_name, company_name, role_in_company, address, email, phone_number]
    
    def number_rows(self):
        print('number_rows - Start')
        number_lines = pd.DataFrame(self.file_xlsx)
        number_lines = len(number_lines.index)
        print('number_rows - End')
        return number_lines

    def open_browser(self):
        print('open_browser - Start')
        self.driver = webdriver.Chrome(executable_path= "C:/Users/thg/Desktop/Projetos/Python/Ex/Ex.004 - RPA Challenge/chromedriver.exe")
        self.driver.implicitly_wait(60)
        self.driver.maximize_window()
        self.driver.get('https://rpachallenge.com/')
        print('open_browser - End')
        
    def name_box(self, input_item):
        print('name_box - Start')
        input_name = self.driver.find_element(By.XPATH, f'(//*[contains(@class, "row")]/div/rpa1-field/div/label)[{input_item}]').get_attribute('textContent')
        print('name_box - End')
        return input_name

    def test_name_box(self, list_data, name_box, element_number):
        
        if name_box.lower() == 'first name':
            self.driver.find_element(By.XPATH, f'(//input)[{element_number}]').send_keys(list_data[0])
        elif name_box.lower() == 'last name':
            self.driver.find_element(By.XPATH, f'(//input)[{element_number}]').send_keys(list_data[1])
        elif name_box.lower() == 'company name':
            self.driver.find_element(By.XPATH, f'(//input)[{element_number}]').send_keys(list_data[2])
        elif name_box.lower() == 'role in company':
            self.driver.find_element(By.XPATH, f'(//input)[{element_number}]').send_keys(list_data[3])
        elif name_box.lower() == 'address':
            self.driver.find_element(By.XPATH, f'(//input)[{element_number}]').send_keys(list_data[4])
        elif name_box.lower() == 'email':
            self.driver.find_element(By.XPATH, f'(//input)[{element_number}]').send_keys(list_data[5])
        elif name_box.lower() == 'phone number':
            self.driver.find_element(By.XPATH, f'(//input)[{element_number}]').send_keys(list_data[6])
        else:
            print('Você fez merda no código, favor revisar...')
    
    def start_challenge(self):
        self.driver.find_element(By.XPATH, '//button').click()
    
    def submit_data(self):
        self.driver.find_element(By.XPATH, '(//input)[8]').click()
    
    def preencher_dados(self):

        def preenchimento(numero_index, linha_planilha):
            dados = self.list_infos(linha_planilha)

            for i in dados:
                input_item = self.name_box(numero_index)
                self.test_name_box(dados, input_item, numero_index)
                numero_index = numero_index + 1

        i = 0
        j = 1
        
        while i < self.number_rows():
            preenchimento(j, i)
            self.submit_data()
            i = i + 1