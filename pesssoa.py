from abc import ABC

class Pessoa(ABC):
    nome: str
    endereco: str
    email: str

    def __init__(self, nome: str, endereco: str, email: str) -> None:
        self.nome = nome
        self.endereco = endereco
        self.email = email