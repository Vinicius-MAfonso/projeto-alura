class Conta:

    def __init__(self, numero, titular, saldo, limite):
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite
        
    def depositar(self, valor):
        self.saldo += valor
    
    def retirar(self, valor):
        self.saldo -= valor
    
    def get_extrato(self, valor):
        print(f"R$ {self.saldo}")
