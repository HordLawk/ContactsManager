from agenda import Agenda
from pessoafisica import PessoaFisica, EstadosCivis
from pessoajuridica import PessoaJuridica
from pesssoa import Pessoa
from datetime import datetime

cmd = -1
while cmd:
    cmd = int(input('Menu:\n0 - Sair\n1 - Adicionar contato\n2 - Remover contato\n3 - Pesquisar por nome\n4 - Pesquisar por CPF/CNPJ\n5 - Listar contatos\n> '))
    if cmd == 1:
        tipo = int(input('\nTipo do contato:\n1 - Pessoa física\n2 - Pessoa jurídica\n> '))
        p: Pessoa
        if tipo == 1:
            nome = input('\nNome: ')
            email = input('Email: ')
            endereco = input('Endereco: ')
            cpf = input('CPF: ')
            tempEstadoCivil = int(input(f'\nEstado civil:\n{EstadosCivis.listar()}\n> '))
            if not tempEstadoCivil in EstadosCivis.values():
                print('\nEstado civil invalido!\n')
                continue
            estadoCivil = EstadosCivis.Valor(tempEstadoCivil)
            dataNascimento = datetime.strptime(input('\nData de nascimento: '), '%d/%m/%Y')
            p = PessoaFisica(nome, endereco, email, cpf, dataNascimento, estadoCivil)
        elif tipo == 2:
            nome = input('\nNome: ')
            email = input('Email: ')
            endereco = input('Endereco: ')
            cnpj = input('CNPJ: ')
            inscricaoEstadual = input('Inscrição estadual: ')
            razaoSocial = input('Razão social: ')
            p = PessoaJuridica(nome, endereco, email, cnpj, inscricaoEstadual, razaoSocial)
        else:
            print('\nTipo invalido!\n')
            continue
        Agenda.adicionar(p)
        print(f'\nContato de {p.nome} foi adicionado\n')
    elif cmd == 2:
        try:
            p = Agenda.remover(input('\nCPF/CNPJ: '))
            print(f'\nContato de {p.nome} foi removido\n')
        except:
            print('\nCPF/CNPJ invalido!\n')
    elif cmd == 3:
        p = Agenda.pesquisarNome(input('\nNome: '))
        if p == None:
            print('\nContato não encontrado!\n')
        else:
            print(f'\n{p}\n')
    elif cmd == 4:
        try:
            p = Agenda.pesquisarKey(input('\nCPF/CNPJ: '))
            print(f'\n{p}\n')
        except:
            print('\nContato não encontrado!\n')
    elif cmd == 5:
        print(f'\n{Agenda.listar()}\n')
    else:
        print()