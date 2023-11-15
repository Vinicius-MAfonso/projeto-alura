class Cliente:

    def __init__(self, nome):
        self.__nome = nome
    
    @property
    def nome(self):
        return self.__nome.title()
    @nome.setter
    def nome(self, nome):
        self.__nome = nome

cliente1 = Cliente("algoz")
print(cliente1.nome)
cliente1.nome = "alfabez"
print(cliente1.nome)