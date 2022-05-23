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