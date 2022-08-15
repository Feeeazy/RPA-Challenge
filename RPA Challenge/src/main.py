from time import sleep
import data_infos

planilha1 = data_infos.Main('C:/Users/thg/Desktop/Projetos/Python/Ex/Ex.004 - RPA Challenge/challenge.xlsx')
planilha1.read_file()
planilha1.start_challenge()
planilha1.preencher_dados()
sleep(100)