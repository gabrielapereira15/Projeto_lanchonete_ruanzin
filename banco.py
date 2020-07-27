import pickle # biblioteca para armazenamento dos dados
import os.path # caminho do sistema operacional

def carregar(valor, nome):
    nomeArquivo = nome + '.obj'
    if os.path.exists(nomeArquivo):
        arquivo = open(nomeArquivo, 'rb')
        return pickle.load(arquivo)
    else:
        return valor

def salvar(valor, nome):
    nomeArquivo = nome + '.obj'
    arquivo = open(nomeArquivo, 'wb')
    pickle.dump(valor, arquivo)