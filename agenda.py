from pesssoa import Pessoa

class Agenda:
    contatos: dict[str, Pessoa] = {}

    @staticmethod
    def adicionar(contato: Pessoa) -> list[Pessoa]:
        Agenda.contatos[contato.nome] = contato
        return Agenda.contatos

    @staticmethod
    def remover(key: str) -> Pessoa:
        p = Agenda.contatos[key]
        Agenda.contatos.pop(key)
        return p

    @staticmethod
    def pesquisarNome(nome: str) -> Pessoa:
        for p in Agenda.contatos.values():
            if p.nome == nome:
                return p

    @staticmethod
    def pesquisarKey(key: str) -> Pessoa:
        pass

    @staticmethod
    def __str__() -> str:
        pass