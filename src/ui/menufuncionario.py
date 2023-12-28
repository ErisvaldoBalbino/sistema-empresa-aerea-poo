from voo.voo import Voo
from voo.pessoa import Passageiro, Tripulante
from voo.reserva import Reserva
from utilities.organizadorcsv import OrganizadorCSV

class MenuFuncionario:
    def __init__(self, organizador):
        self.organizador = organizador

    def exibir_menu(self):
        while True:
            print("\n1. Cadastrar Passageiro")
            print("2. Ver Passageiros")
            print("3. Cadastrar Reserva")
            print("4. Ver Reservas")
            print("5. Remover Reserva")
            print("6. Remover Passageiro")
            print("7. Salvar Voo")
            print("8. Listar Voos")
            print("9. Cadastrar Tripulante")
            print("10. Associar Tripulante a Voo")
            print("11. Ver Tripulantes")
            print("12. Remover Tripulante")
            print("13. Sair")

            escolha = input("Escolha uma opção: ")

            if escolha == '1':
                self.cadastrar_passageiro()
            elif escolha == '2':
                self.visualizar_passageiros()
            elif escolha == '3':
                self.cadastrar_reserva()
            elif escolha == '4':
                self.visualizar_reservas()
            elif escolha == '5':
                self.remover_reserva()
            elif escolha == '6':
                self.remover_passageiro()
            elif escolha == '7':
                self.salvar_voo()
            elif escolha == '8':
                self.listar_voos()
            elif escolha == '9':
                self.cadastrar_tripulante()
            elif escolha == '10':
                self.associar_tripulante_voo()
            elif escolha == '11':
                self.visualizar_tripulantes()
            elif escolha == '12':
                self.remover_tripulante()
            elif escolha == '13':
                print("Saindo...")
                break
            else:
                print("Opção inválida. Tente novamente.")

    def cadastrar_passageiro(self):
        nome = input("Digite o nome do passageiro: ")
        cpf = input("Digite o CPF do passageiro: ")
        telefone = input("Digite o telefone do passageiro: ")

        passageiro = Passageiro(nome, cpf, telefone)
        self.organizador.salvarPassageiro(passageiro)
        print(f"Passageiro {nome} cadastrado com sucesso.")

    def visualizar_passageiros(self):
        passageiros = self.organizador.carregarPassageiros()
        if passageiros:
            print("\nPassageiros:")
            for passageiro in passageiros:
                print(f"Nome: {passageiro['nome']}, CPF: {passageiro['cpf']}, Telefone: {passageiro['telefone']}")
        else:
            print("Nenhum passageiro cadastrado.")

    def remover_passageiro(self):
        cpf = input("Digite o CPF do passageiro a ser removido: ")
        passageiros = self.organizador.carregarPassageiros()
        if any(passageiro['cpf'] == cpf for passageiro in passageiros):
            reservas = self.organizador.carregarReservas()
            if any(reserva['cpf'] == cpf for reserva in reservas):
                print(f"Passageiro com CPF {cpf} não pode ser removido pois possui reservas.")
            else:
                self.organizador.removerPassageiro(cpf)
                print(f"Passageiro com CPF {cpf} removido com sucesso.")
        else:
            print(f"Passageiro com CPF {cpf} não encontrado.")

    def cadastrar_reserva(self):
        cpf = input("Digite o CPF do passageiro: ")

        self.listar_voos()

        voo_codigo = input("Digite o código do voo: ")
        assento = input("Digite o assento (ID) da reserva: ")
        voo_info = self.organizador.obterVooPorCodigo(voo_codigo)

        passageiros = self.organizador.carregarPassageiros()

        # procura o passageiro na lista
        passageiro_encontrado = next((passageiro for passageiro in passageiros if passageiro['cpf'] == cpf), None)

        if passageiro_encontrado and voo_info:
            voo = Voo(voo_info['codigo'], voo_info['tipo'], voo_info['data'], voo_info['partida'], voo_info['destino'], voo_info['aviao'])

            reserva = Reserva(passageiro_encontrado, voo, assento)
            self.organizador.salvarReservaPassageiro(reserva)
            print(f"Reserva para o voo {voo_codigo} cadastrada com sucesso.")
        elif not voo_info:
            print(f"Voo {voo_codigo} não encontrado.")
        else:
            print(f"Passageiro com CPF {cpf} não encontrado.")

    def visualizar_reservas(self):
        reservas = self.organizador.carregarReservas()
        if reservas:
            print("\nReservas:")
            for reserva in reservas:
                print(f"CPF: {reserva['cpf']}, Voo: {reserva['voo']}, Assento (ID): {reserva['assento']}")
        else:
            print("Nenhuma reserva cadastrada.")

    def remover_reserva(self):
        assento = input("Digite o assento (ID) da reserva a ser removida: ")
        if self.organizador.removerReserva(assento):
            print(f"Reserva para o assento {assento} removida com sucesso.")
        else:
            print(f"Reserva para o assento {assento} não encontrada.")

    def salvar_voo(self):
        codigo = input("Digite o código do voo: ")
        tipo = input("Digite o tipo do voo: ")
        data = input("Digite a data do voo: ")
        partida = input("Digite o aeroporto de partida: ")
        destino = input("Digite o aeroporto de destino: ")
        aviao = input("Digite o avião: ")

        voo = Voo(codigo, tipo, data, partida, destino, aviao)
        self.organizador.salvarVoo(voo)
        print(f"Voo {codigo} cadastrado com sucesso.")

    def listar_voos(self):
        voos = self.organizador.carregarVoos()
        if voos:
            print("\nVoos:")
            for voo in voos:
                print(f"Código: {voo['codigo']}, Tipo: {voo['tipo']}, Data: {voo['data']}, Partida: {voo['partida']}, Destino: {voo['destino']}, Avião: {voo['aviao']}")
        else:
            print("Nenhum voo cadastrado.")

    def cadastrar_tripulante(self):
        nome = input("Digite o nome do tripulante: ")
        cpf = input("Digite o CPF do tripulante: ")
        funcao = input("Digite a funcao do tripulante: ")

        tripulante = Tripulante(nome, cpf, funcao)
        self.organizador.salvarTripulante(tripulante)
        print(f"Tripulante {nome} cadastrado com sucesso.")

    def associar_tripulante_voo(self):
        cpf = input("Digite o CPF do tripulante: ")

        self.listar_voos()

        voo_codigo = input("Digite o código do voo: ")
        voo_info = self.organizador.obterVooPorCodigo(voo_codigo)

        tripulantes = self.organizador.carregarTripulantes()

        # procura o tripulante na lista
        tripulante_encontrado = next((tripulante for tripulante in tripulantes if tripulante['cpf'] == cpf), None)

        if tripulante_encontrado and voo_info:
            Voo(voo_info['codigo'], voo_info['tipo'], voo_info['data'], voo_info['partida'], voo_info['destino'], voo_info['aviao'])

            tripulante = Tripulante(tripulante_encontrado['nome'], tripulante_encontrado['cpf'], tripulante_encontrado['funcao'], voo_codigo)
            self.organizador.removerTripulante(cpf)
            self.organizador.salvarTripulante(tripulante)
            print(f"Tripulante {tripulante_encontrado['nome']} associado ao voo {voo_codigo} com sucesso.")
        elif not voo_info:
            print(f"Voo {voo_codigo} não encontrado.")
        else:
            print(f"Tripulante com CPF {cpf} não encontrado.")

    def visualizar_tripulantes(self):
        tripulantes = self.organizador.carregarTripulantes()
        if tripulantes:
            print("\nTripulantes:")
            for tripulante in tripulantes:
                voo_codigo = tripulante['voo']['codigo'] if 'voo' in tripulante and 'codigo' in tripulante['voo'] else ''
                print(f"Nome: {tripulante['nome']}, CPF: {tripulante['cpf']}, Função: {tripulante['funcao']}, Voo: {voo_codigo}")
        else:
            print("Nenhum tripulante cadastrado.")

    def remover_tripulante(self):
        cpf = input("Digite o CPF do tripulante a ser removido: ")
        tripulantes = self.organizador.carregarTripulantes()
        if any(tripulante['cpf'] == cpf for tripulante in tripulantes):
            self.organizador.removerTripulante(cpf)
            print(f"Tripulante com CPF {cpf} removido com sucesso.")
        else:
            print(f"Tripulante com CPF {cpf} não encontrado.")