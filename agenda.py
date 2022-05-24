from pesssoa import Pessoa
from pessoajuridica import PessoaJuridica

class Agenda:
    contatos: dict[str, Pessoa] = {}

    @staticmethod
    def adicionar(contato: Pessoa) -> dict[str, Pessoa]:
        Agenda.contatos[contato.getKey()] = contato
        return Agenda.contatos

    @staticmethod
    def remover(key: str) -> Pessoa:
        p: Pessoa = Agenda.contatos[key]
        Agenda.contatos.pop(key)
        return p

    @staticmethod
    def pesquisarNome(nome: str) -> Pessoa:
        for p in Agenda.contatos.values():
            if p.nome == nome:
                return p

    @staticmethod
    def pesquisarKey(key: str) -> Pessoa:
        return Agenda.contatos[key]

    @staticmethod
    def listar() -> str:
        return '\n'.join([str(x) for x in Agenda.__ordena()])

    @staticmethod
    def __ordena() -> list[Pessoa]:
        contatosOrdenados: list[Pessoa] = list(Agenda.contatos.values())
        for i, e in enumerate(contatosOrdenados):
            j: int = i - 1
            while j >=0 and ((isinstance(e, PessoaJuridica) < isinstance(contatosOrdenados[j], PessoaJuridica)) or (e.getKey() < contatosOrdenados[j].getKey())):
                    contatosOrdenados[j + 1] = contatosOrdenados[j]
                    j -= 1
            contatosOrdenados[j + 1] = e
        return contatosOrdenados