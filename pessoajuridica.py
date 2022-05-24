from pesssoa import Pessoa

class PessoaJuridica(Pessoa):
    cnpj: str
    inscricaoEstadual: str
    razaoSocial: str

    def __init__(self, nome: str, endereco: str, email: str, cnpj: str, inscricaoEstadual: str, razaoSocial: str) -> None:
        super().__init__(nome, endereco, email)
        self.cnpj = cnpj
        self.inscricaoEstadual = inscricaoEstadual
        self.razaoSocial = razaoSocial

    def getKey(self) -> str:
        return self.cnpj

    def __str__(self) -> str:
        return super().__str__() + f'CNPJ: {self.cnpj}\nInscrição Estadual: {self.inscricaoEstadual}\nRazão Social: {self.razaoSocial}\n'