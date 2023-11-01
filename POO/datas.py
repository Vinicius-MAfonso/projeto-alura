class Data:
    def __init__(self, dia, mes, ano):
        self.dia = dia
        self.mes = mes
        self.ano = ano
    
    def formatata(self):
        print(f"{self.dia}/{self.mes}/{self.ano}")

data = Data(23,10,2023)
data.formatata()