from funções import arquivo

def linha(tam = 40):
    return '-' * tam

def cabeçalho(texto):
    print(linha())
    print(texto.center(40))
    print(linha())

def escolhaUsuario(numero):
    if numero == 1:
        cabeçalho("PESSOAS CADASTRADAS")
        arquivo.lerArquivo('dados.txt')
    elif numero == 2:
        cabeçalho("CADASTRAMENTO")
        nome = str(input("Nome: "))
        while True:
            try:
                idade = int(input("Idade: "))
            except (ValueError, TypeError):
                print("\033[31mERRO: Informe sua idade com números inteiros!\033[m")
                continue
            else:
                break
        arquivo.cadastrar('dados.txt', nome, idade)
    elif numero == 3:
        cabeçalho("Saindo do sistema... Até logo!")
        exit()

def tratamentoErro(lista):
    while True:
        try:
            n = int(input("\033[32mSua opção: \033[m"))
            while n <= 0 or n > len(lista):
                print("\033[31mERRO: Digite uma opção válida!\033[m") 
                n = int(input("\033[32mSua opção: \033[m"))
        except (ValueError, TypeError):
            print("\033[31mERRO: Por favor, digite um número inteiro válido\033[m")
            continue
        else:
            escolhaUsuario(n)
        cabeçalho("MENU PRINCIPAL")
        for pos, i in enumerate(lista):
            print(f"\033[33m{pos + 1}\033[m - \033[34m{i}\033[m")
        print(linha())       

def menu(lista):
    cabeçalho("MENU PRINCIPAL")
    for pos, i in enumerate(lista):
        print(f"\033[33m{pos + 1}\033[m - \033[34m{i}\033[m")
    print(linha())
    tratamentoErro(lista)


    





        