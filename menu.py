from cadastro_cliente import CadastroCliente
from cadastro_pedido import CadastroPedido
from cadastro_produto import CadastroProduto
import banco

print("***BEM-VINDO À RUANZIN LANCHES***")

cpe = CadastroPedido()
cc = CadastroCliente()
cpr = CadastroProduto()

cpe.pedidos = banco.carregar(cpe.pedidos, "pedidos")
cc.clientes = banco.carregar(cc.clientes, "clientes")
cpr.produtos = banco.carregar(cpr.produtos, "produtos")

while True:
    print("********* MENU INICIAL **********")
    print("ESCOLHA A OPÇÃO")
    print("'1' PARA CADASTRAR OU ALTERAR UM PEDIDO")
    print("'2' PARA CADASTRAR/ALTERAR OU EXCLUIR UM CLIENTE")
    print("'3' PARA CADASTRAR/ALTERAR OU EXCLUIR UM PRODUTO")
    print("'4' PARA IMPRIMIR UM RELATÓRIO")
    print("'0' SALVAR OS DADOS E SAIR DO SISTEMA")
    opcao = int(input("QUAL OPÇÃO DESEJADA:"))

    if(opcao == 1):
        print("CADASTRAR OU ALTERAR UM PEDIDO")
        print("'1' PARA CADASTRAR UM PEDIDO")
        print("'2' PARA ALTERAR UM PEDIDO")
        #print("'3' PARA EXCLUIR UM PEDIDO")
        opcao_pedido = int(input("Qual opção desejada:"))
        if (opcao_pedido == 1):
            cpf = input("Por favor, digite o CPF do cliente (sem pontos, exemplo: 12345678900):")
            cpf = '{}.{}.{}-{}'.format(cpf[:3], cpf[3:6], cpf[6:9], cpf[9:])
            cliente = cc.buscar_cliente(cpf)
            if cliente is not None:
                print("Cliente,",cliente.nome,"encontrado(a)")
            else:
                print("Cliente não cadastrado, será necessário cadastrar")
                cliente = cc.cadastrar_cliente()
            #APÓS VERIFICAR SE HÁ CADASTRO DO CLIENTE OU NÃO, EFETUAR O CADASTRO DO PEDIDO
            produtos = []
            qtds = []
            while True:
                nome = input("Informe o nome do produto desejado ou F para finalizar e retornar ao Menu:")
                if nome == "F":
                    break
                produto = cpr.buscar_produto(nome)
                if produto is not None:
                    qntd = input("Qual a quantidade:")
                    produtos.append(produto)
                    qtds.append(qntd)
                else:
                    print("Produto não cadastrado!")

            pedido = cpe.cadastrar_pedido(cliente, produtos, qtds)
            print("RESUMO DO PEDIDO - Cliente:", cliente.nome)
            for p,q in zip(pedido.produtos, pedido.quantidades):
                print("PRODUTO:", p.nome, "QNTD:", q)

        elif (opcao_pedido == 2):
            cpe.editar_pedido(cpr)
        #elif (opcao_cliente == 3):
            #cc.excluir_cliente()
            #verificar se o cliente já está cadastrado

    elif(opcao == 2):
        print("CADASTRAR/ALTERAR/EXCLUIR UM CLIENTE")
        print("'1' PARA CADASTRAR UM CLIENTE")
        print("'2' PARA ALTERAR UM CLIENTE")
        print("'3' PARA EXCLUIR UM CLIENTE")
        opcao_cliente = int(input("Qual opção desejada:"))
        if (opcao_cliente == 1):
            cc.cadastrar_cliente()
        elif (opcao_cliente == 2):
            cc.editar_cliente()
        elif(opcao_cliente == 3):
            cc.excluir_cliente()

    elif(opcao == 3):
        print("CADASTRAR/ALTERAR/EXCLUIR UM PRODUTO")
        print("'1' PARA CADASTRAR UM PRODUTO")
        print("'2' PARA ALTERAR UM PRODUTO")
        print("'3' PARA EXCLUIR UM PRODUTO")
        opcao_produto = int(input("Qual opção desejada:"))
        if (opcao_produto == 1):
            cpr.cadastrar_produtos()
        elif (opcao_produto == 2):
            cpr.editar_produto()
        elif (opcao_produto == 3):
            cpr.excluir_produto()

    elif(opcao == 4):
        print("IMPRIMIR RELATÓRIO")
        print("'1' PARA QUANTIDADE TOTAL EM PEDIDOS ATÉ O MOMENTO")
        print("'2' PARA QUANTIDADE TOTAL DE PEDIDOS POR CLIENTE")
        print("'3' PARA QUANTIDADE TOTAL DE PEDIDOS POR PRODUTO")
        print("'4' PARA TOTAL EM REAIS FATURADOS ATÉ O MOMENTO")
        print("'5' PARA LISTA DE CLIENTES")
        print("'6' PARA LISTA DE PRODUTOS")
        opcao_relatorio = int(input("QUAL OPÇÃO DESEJADA:"))
        if(opcao_relatorio == 1):
            cpe.relatorio_pedidos()
        elif(opcao_relatorio == 2):
            cpe.relatorio_pedido_cliente()
        elif(opcao_relatorio == 3):
            cpe.relatorio_pedido_produto()
        elif(opcao_relatorio == 4):
            cpe.relatorio_faturamento()
        elif(opcao_relatorio == 5):
            cc.relatorio_clientes()
        elif(opcao_relatorio == 6):
            cpr.relatorio_produtos()

    elif(opcao == 0):
        banco.salvar(cpe.pedidos, "pedidos")
        banco.salvar(cc.clientes, "clientes")
        banco.salvar(cpr.produtos, "produtos")
        break