from pedido import Pedido
from cadastro_produto import CadastroProduto
from produto import Produto
from collections import Counter

class CadastroPedido:

    pedidos = []

    def cadastrar_pedido(self, cliente, produtos, quantidades):
        pedido = Pedido(cliente,produtos,quantidades)
        self.pedidos.append(pedido)
        return pedido

    def editar_pedido(self, cpr):
        cpf = input("Digite o CPF do cliente que deseja alterar o pedido:")
        if len(cpf) < 11:
            cpf = cpf.zfill(11)
        cpf = '{}.{}.{}-{}'.format(cpf[:3], cpf[3:6], cpf[6:9], cpf[9:])
        pedido = self.pedido_por_cliente(cpf)
        if pedido is not None:
            print("PEDIDO ENCONTRADO!")
            print("'1' PARA ADICIONAR UM PRODUTO")
            #print("'2' PARA EXCLUIR UM PRODUTO")
            opcao_pedido = int(input("Qual opção desejada:"))
            if(opcao_pedido == 1):
                nome = input("Informe o nome do produto que deseja adicionar no pedido:")
                produto = cpr.buscar_produto(nome)
                if produto is not None:
                    qntd = input("Qual a quantidade:")
                    pedido.produtos.append(produto)
                    pedido.quantidades.append(qntd)
                    print("RESUMO DO PEDIDO ALTERADO - Cliente:", pedido.cliente.nome)
                    for p, q in zip(pedido.produtos, pedido.quantidades):
                        print("PRODUTO:", p.nome, "QNTD:", q)
                else:
                    print("Produto não cadastrado!")
            #elif(opcao_pedido == 2):
        else:
            print("Cliente não possui pedido cadastrado!")

    #def excluir_pedido(self):

    def pedido_por_cliente(self, cpf):
        for pedido in self.pedidos:
            if pedido.cliente.cpf == cpf:
                return pedido

    def relatorio_pedidos(self):
        print("QUANTIDADE DE PEDIDOS CADASTRADOS ATÉ O MOMENTO:", len(self.pedidos))

    def relatorio_pedido_cliente(self):
        clientes = []
        for pedido in self.pedidos:
            clientes.append(pedido.cliente.cpf)
        print("QUANTIDADE TOTAL DE PEDIDOS PARA CADA CLIENTE:")
        print(Counter(clientes))

    def relatorio_pedido_produto(self):
        produtos = []
        for pedido in self.pedidos:
            for produto in pedido.produtos:
                produtos.append(produto.nome)
        print("QUANTIDADE TOTAL DE PEDIDOS PARA CADA PRODUTO:")
        print(Counter(produtos))

    def relatorio_faturamento(self):
        soma_faturamento = 0
        for pedido in self.pedidos:
            for produto in pedido.produtos:
                soma_faturamento += produto.preco_unitario
        print("O VALOR TOTAL EM REAIS FATURADOS ATÉ O MOMENTO É R$", soma_faturamento)

