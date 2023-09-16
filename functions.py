contatos = []


def validacao(txt, respValida, tipo):
    #Função é para validar os valores
    n = input(txt).capitalize()
    if n not in respValida or n == '':
        n = input(f'[VALOR INVÁLIDO] {txt}')
    
    if tipo == 1:
        return int(n)
    
    else:
        return n


def procurarContato(txt):
    #Função para procurar o nome e a posição do contato escolhido
    nomeContato = [pessoas['Nome'] for pessoas in contatos]
    n = validacao(txt, nomeContato, 2)

    for pos, valor in enumerate(contatos):
        if valor['Nome'] == n:
            dados = [n, pos]

    return dados


def criarContatos():
    #Função para criar contatos e adicioná-los em uma lista
    info = {
        'Nome': input('Nome do contato: '),
        'Email': input('Email do contato: '),
        'Número': input('Número do contato: ')
    }
    contatos.append(info)


def listarContatos():
    #Função para mostrar os contatos
    if len(contatos) > 0:
        print('Lista de contatos: ')
        for pos, valor in enumerate(contatos):
            print(f'{pos} : {valor}')
    else: 
        print('\nVocê ainda não tem contatos\n')
    

def editarContatos():
    #Função para a opção do menu de editar contatos
    listarContatos()
    edt = procurarContato('Qual contato deseja editar? ')
    opc = validacao(f'O que deseja editar do contato {edt[0]}?\nNome\nEmail\nNúmero\n',['Nome','Email','Número'], 2)
    contatos[edt[1]][opc] = input('Coloque aqui a atualização: ')


def excluirContato():
    #Função para a opção do menu de excluir contatos
    listarContatos()
    exc = procurarContato('Qual contato deseja excluir? ')
    contatos.pop(exc[1])
    

def menu():
    #Função para o menu de opções
    resp = validacao('Digite:\n[1] - Adicionar um novo contato\n[2] - Listar todos os contatos\n[3] - Atualizar informações de um contato\n[4] - Excluir um contato.\n[5] - Sair\n', ['1', '2', '3', '4', '5'], 1)

    if resp == 1:
        criarContatos()

    elif resp == 2:
        listarContatos()

    elif resp == 3:
        editarContatos()

    elif resp == 4:
        excluirContato()

    elif resp == 5:
        return False
        
    return True