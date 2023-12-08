from rich import print

class Programa:
    def __init__(self, titulo:str, ano:int):
        self._titulo = titulo.title()
        self.ano = ano
    @property
    def titulo(self):
        return self._titulo
    @titulo.setter
    def titulo(self, titulo:str):
        self._titulo = titulo.title()
    def __repr__(self) -> str:
        return f"Titulo: {self.titulo}, Ano: {self.ano}"
    


class Filme(Programa):
    def __init__(self, titulo:str, ano:int, duracao:float):
        super().__init__(titulo, ano)
        self.duracao = duracao
    def __repr__(self) -> str:
        return super().__repr__() + f", Duracao: {self.duracao}"
    


class Serie(Programa):
    def __init__(self, titulo:str, ano:int, temporadas:int):
        super().__init__(titulo, ano)
        self.temporadas = temporadas
    def __repr__(self) -> str:
        return super().__repr__() + f", Temporadas: {self.temporadas}"


class Playlist:
    def __init__(self, nome, programas):
        self._programas = programas
        self.nome = nome

    def __getitem__(self, item):
        return self._programas[item]

    @property
    def listagem(self):
        return len(self._programas)

    @property
    def tamanho(self):
        return len(self._programas)
    def __len__(self):
        return len(self.programas)


if __name__ == "__main__":
    filme = Filme("Viagem de Guliver", 2002, 2.30)
    serie = Serie("Dr House", 2010, 7)
    playlist = Playlist("minha", [filme, serie])
    for programa in playlist:
        print(programa)