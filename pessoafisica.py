from enum import Enum
import datetime
from pesssoa import Pessoa

class PessoaFisica(Pessoa):
    EstadosCivis: Enum = Enum('EstadosCivis', ['Solteiro(a)', 'Casado(a)', 'Separado(a)', 'Divorciado(a)', 'Viúvo(a)'])

    cpf: str
    dataDeNascimento: datetime.date
    estadoCivil: EstadosCivis

    def __init__(self, nome: str, endereco: str, email: str, cpf: str, dataDeNascimento: datetime.date, estadoCivil: EstadosCivis) -> None:
        super().__init__(nome, endereco, email)
        self.cpf = cpf
        self.dataDeNascimento = dataDeNascimento
        self.estadoCivil = estadoCivil