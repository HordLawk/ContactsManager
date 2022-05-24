from enum import Enum
from datetime import datetime
from pesssoa import Pessoa

class EstadosCivis:
    Valor = Enum('EstadosCivis', ['Solteiro(a)', 'Casado(a)', 'Separado(a)', 'Divorciado(a)', 'Viúvo(a)'])
    
    @staticmethod
    def listar() -> str:
        return '\n'.join([f'{x.value} - {x.name}' for x in EstadosCivis.Valor])

    @staticmethod
    def values() -> list[int]:
        return [x.value for x in EstadosCivis.Valor]

class PessoaFisica(Pessoa):
    cpf: str
    dataDeNascimento: datetime
    estadoCivil: EstadosCivis.Valor

    def __init__(self, nome: str, endereco: str, email: str, cpf: str, dataDeNascimento: datetime, estadoCivil: EstadosCivis.Valor) -> None:
        super().__init__(nome, endereco, email)
        self.cpf = cpf
        self.dataDeNascimento = dataDeNascimento
        self.estadoCivil = estadoCivil
    
    def getKey(self) -> str:
        return self.cpf

    def __str__(self) -> str:
        return super().__str__() + f'CPF: {self.cpf}\nData de Nascimento: {self.dataDeNascimento.date()}\nEstado Civil: {self.estadoCivil.name}\n'