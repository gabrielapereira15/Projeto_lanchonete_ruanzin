from cliente import Cliente

class CadastroCliente:

    clientes = []

    def cadastrar_cliente(self):
        while True:
            nome = input("Digite o nome do cliente ou R para retornar ao Menu Inicial:")
            if nome == "R":
                break
            cpf = input("Digite o CPF do cliente (sem pontos, exemplo: 12345678900):")
            if len(cpf) < 11:
                cpf = cpf.zfill(11)
            cpf = '{}.{}.{}-{}'.format(cpf[:3], cpf[3:6], cpf[6:9], cpf[9:])
            cliente = Cliente(nome, cpf)
            self.clientes.append(cliente)
            print("Ok! Cliente cadastrado.")
            return cliente

    def editar_cliente(self):
        cpf_editar = input("Digite o CPF do cliente que deseja alterar:")
        if len(cpf_editar) < 11:
            cpf_editar = cpf_editar.zfill(11)
        cpf_editar = '{}.{}.{}-{}'.format(cpf_editar[:3], cpf_editar[3:6], cpf_editar[6:9], cpf_editar[9:])
        cliente = self.buscar_cliente(cpf_editar)
        nome_editado = input("Digite o nome do cliente alterado:")
        cpf_editado = input("Digite o CPF do cliente alterado:")
        if len(cpf_editado) < 11:
            cpf_editado = cpf_editado.zfill(11)
        cpf_editado = '{}.{}.{}-{}'.format(cpf_editado[:3], cpf_editado[3:6], cpf_editado[6:9], cpf_editado[9:])
        cliente.nome = nome_editado
        cliente.cpf = cpf_editado
        print("Ok! Cliente alterado.")

    def excluir_cliente(self):
        cpf_excluir = input("Digite o CPF do cliente que deseja excluir:")
        if len(cpf_excluir) < 11:
            cpf_excluir = cpf_excluir.zfill(11)
        cpf_excluir = '{}.{}.{}-{}'.format(cpf_excluir[:3], cpf_excluir[3:6], cpf_excluir[6:9], cpf_excluir[9:])
        cliente = self.buscar_cliente(cpf_excluir)
        self.clientes.remove(cliente)
        print("Ok! Cliente excluido.")

    def buscar_cliente(self, cpf):
        for cliente in self.clientes:
            if cliente.cpf == cpf:
                return cliente

    def relatorio_clientes(self):
        print("LISTA DE CLIENTES - RUANZIN LANCHES:")
        for p in self.clientes:
            print(p.nome,"- CPF:",p.cpf)
        print("Quantidade de clientes cadastrados:", len(self.clientes))
