import pandas as pd
from .var_fixas import *

class ArquivoChallenge:
    def __init__(self, file):
        self.file = file
    def ler_arquivo(self):
        dados = pd.read_excel(self.file)
        return dados