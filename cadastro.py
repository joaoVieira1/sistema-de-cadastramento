from funções import lib
from funções import arquivo

arq = 'dados.txt'

if not arquivo.arquivoExiste(arq):
    arquivo.criarArquivo(arq)

lib.menu(["Ver pessoas cadastradas", "Cadastrar nova pessoa", "Sair do sistema"])


