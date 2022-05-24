from agenda import Agenda
from pessoafisica import PessoaFisica, EstadosCivis
from pessoajuridica import PessoaJuridica
from pesssoa import Pessoa
from datetime import datetime

cmd: int = -1
while cmd != 0:
    cmd = int(input('Menu:\n0 - Sair\n1 - Adicionar contato\n2 - Remover contato\n3 - Pesquisar por nome\n4 - Pesquisar por CPF/CNPJ\n5 - Listar contatos\n> '))
    if cmd == 1:
        tipo: int = int(input('\nTipo do contato:\n1 - Pessoa física\n2 - Pessoa jurídica\n> '))
        p: Pessoa
        if tipo == 1:
            nome: str = input('\nNome: ')
            email: str = input('Email: ')
            endereco: str = input('Endereco: ')
            cpf: str = input('CPF: ')
            tempEstadoCivil: int = int(input('\nEstado civil:\n{}\n> '.format(EstadosCivis.listar())))
            if not tempEstadoCivil in EstadosCivis.values():
                print('\nEstado civil invalido!\n')
                continue
            estadoCivil: EstadosCivis.Valor = EstadosCivis.Valor(tempEstadoCivil)
            dataNascimento: datetime = datetime.strptime(input('\nData de nascimento: '), '%d/%m/%Y')
            p = PessoaFisica(nome, endereco, email, cpf, dataNascimento, estadoCivil)
        elif tipo == 2:
            nome: str = input('\nNome: ')
            email: str = input('Email: ')
            endereco: str = input('Endereco: ')
            cnpj: str = input('CNPJ: ')
            inscricaoEstadual: str = input('Inscrição estadual: ')
            razaoSocial: str = input('Razão social: ')
            p = PessoaJuridica(nome, endereco, email, cnpj, inscricaoEstadual, razaoSocial)
        else:
            print('\nTipo invalido!\n')
            continue
        Agenda.adicionar(p)
        print('\nContato de {} foi adicionado\n'.format(p.nome))
    elif cmd == 2:
        try:
            p: Pessoa = Agenda.remover(input('\nCPF/CNPJ: '))
            print('\nContato de {} foi removido\n'.format(p.nome))
        except:
            print('\nCPF/CNPJ invalido!\n')
    elif cmd == 3:
        p = Agenda.pesquisarNome(input('\nNome: '))
        if p == None:
            print('\nContato não encontrado!\n')
        else:
            print('\n{}\n'.format(p))
    elif cmd == 4:
        try:
            p = Agenda.pesquisarKey(input('\nCPF/CNPJ: '))
            print('\n{}\n'.format(p))
        except:
            print('\nContato não encontrado!\n')
    elif cmd == 5:
        print('\n{}\n'.format(Agenda.listar()))
    else:
        print()