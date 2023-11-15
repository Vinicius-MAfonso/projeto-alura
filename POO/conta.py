class Conta:

    def __init__(self, numero, titular, saldo, limite):
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo        #Atributos privados
        self.__limite = limite
        
    def deposita(self, valor):
        self.__saldo += valor
    
    def __pode_sacar(self, valor): #Método privado
        pass

    def sacar(self, valor):
        if(valor <= (self.__saldo + self.__limite)):
            self.__saldo -= valor
        else:
            print("Valor + limite insuficiente")

    def transferir(self, destino, valor):
        self.sacar(valor)
        destino.deposita(valor)    
    
    @property                   #"Getters" e "Setters"
    def numero(self):
        return self.__numero
    
    @property
    def titular(self):
        return self.__titular
    
    @property
    def saldo(self):
        return f"R$ {self.__saldo}"

    @property
    def limite(self):
        return self.__limite
    
    @limite.setter
    def limite(self, limite):
        self.__limite = limite

    @staticmethod
    def codigo_banco():
        return "001"