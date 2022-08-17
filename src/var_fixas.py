import os

#Diretório onde está localizado o path do chromedriver
CHROME_DRIVER_PATH = r'bin\chromedriver.exe'

#Url do site RPA Challenge
URL_CHALLENGE = 'https://rpachallenge.com/'

#Valor fixo da função implicitly_wait em segundos
IMPLICITY_WAIT = 60

# Decide se o browser será maximizado ou não
MAXIMIZAR = True

# Link para download da planilha do desafio
URL_DOWNLOAD_SHEET = 'https://rpachallenge.com/assets/downloadFiles/challenge.xlsx'

# Diretório onde a planilha do desafio será baixada
DIRETORIO_DOWNLOAD = os.path.join(os.path.expanduser('~'), 'Downloads', 'challenge.xlsx')

# Diretório onde deve estar para ser executado
DIRETORIO_BIN = os.path.join('C:/GIT/Python/RPA-Challenge/bin', 'challenge.xlsx')