from produto import Produto

class CadastroProduto:

    produtos = []

    def cadastrar_produtos(self):

        while True:
            nome = input("Digite o nome do produto ou R para retornar ao Menu Inicial:")
            if nome == "R":
                break
            preco_unitario = float(input("Digite o preço do produto:"))
            self.produtos.append(Produto(nome, preco_unitario))
            print("Ok! Próximo produto.")

    def editar_produto(self):
        produto_editar = input("Digite o nome do produto que deseja alterar:")
        produto = self.buscar_produto(produto_editar)
        produto_editado = input("Digite o nome do produto alterado:")
        preco_editado = input("Digite o preço do produto alterado:")
        produto.nome = produto_editado
        produto.preco_unitario = preco_editado
        print("Ok! Produto alterado.")

    def excluir_produto(self):
        produto_excluir = input("Digite o nome do produto que deseja excluir:")
        produto = self.buscar_produto(produto_excluir)
        self.produtos.remove(produto_excluir)
        print("Ok! Produto excluido.")

    def buscar_produto(self, nome):
        for produto in self.produtos:
            if produto.nome == nome:
                return produto

    def relatorio_produtos(self):
        print("LISTA DE PRODUTOS - RUANZIN LANCHES:")
        for p in self.produtos:
            print(p.nome,":",p.preco_unitario)
        print("QUANTIDADE DE PRODUTOS CADASTRADOS:", len(self.produtos))

