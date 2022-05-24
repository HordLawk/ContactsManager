from abc import ABC, abstractmethod

class Pessoa(ABC):
    nome: str
    endereco: str
    email: str

    def __init__(self, nome: str, endereco: str, email: str) -> None:
        self.nome = nome
        self.endereco = endereco
        self.email = email

    @abstractmethod
    def getKey(self) -> str:
        pass
    
    def __str__(self) -> str:
        return 'Nome: {}\nEndereço: {}\nEmail: {}\n'.format(self.nome, self.endereco, self.email)