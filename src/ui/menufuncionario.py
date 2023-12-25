from voo.voo import Voo
from voo.passageiro import Passageiro
from voo.reserva import Reserva
from utilities.organizadorcsv import OrganizadorCSV

class MenuFuncionario:
    def __init__(self, organizador):
        self.organizador = organizador

    def exibir_menu(self):
        while True:
            print("\n1. Cadastrar Passageiro")
            print("2. Visualizar Passageiros")
            print("3. Cadastrar Reserva")
            print("4. Visualizar Reservas")
            print("5. Remover Reserva")
            print("6. Remover Passageiro")
            print("7. Salvar Voo")
            print("8. Listar Voos")
            print("9. Sair")

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
        voo_info = self.organizador.obterVooPorCodigo(voo_codigo)

        passageiros = self.organizador.carregarPassageiros()

        # procura o passageiro na lista
        passageiro_encontrado = next((passageiro for passageiro in passageiros if passageiro['cpf'] == cpf), None)

        if passageiro_encontrado and voo_info:
            voo = Voo(voo_info['codigo'], voo_info['tipo'], voo_info['data'], voo_info['partida'], voo_info['destino'], voo_info['aviao'], voo_info['assentosTotais'])

            reserva = Reserva(passageiro_encontrado, voo)
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
                print(f"CPF: {reserva['cpf']}, Voo: {reserva['voo']}, ID: {reserva['id']}")
        else:
            print("Nenhuma reserva cadastrada.")

    def remover_reserva(self):
        id_reserva = input("Digite o ID da reserva a ser removida: ")
        if self.organizador.removerReserva(id_reserva):
            print(f"Reserva com ID {id_reserva} removida com sucesso.")
        else:
            print(f"Reserva com ID {id_reserva} não encontrada.")

    def salvar_voo(self):
        codigo = input("Digite o código do voo: ")
        tipo = input("Digite o tipo do voo: ")
        data = input("Digite a data do voo: ")
        partida = input("Digite o aeroporto de partida: ")
        destino = input("Digite o aeroporto de destino: ")
        aviao = input("Digite o avião: ")
        assentos = input("Digite o número de assentos: ")

        voo = Voo(codigo, tipo, data, partida, destino, aviao, assentos)
        self.organizador.salvarVoo(voo)
        print(f"Voo {codigo} cadastrado com sucesso.")

    def listar_voos(self):
        voos = self.organizador.carregarVoos()
        if voos:
            print("\nVoos:")
            for voo in voos:
                print(f"Código: {voo['codigo']}, Tipo: {voo['tipo']}, Data: {voo['data']}, Partida: {voo['partida']}, Destino: {voo['destino']}, Avião: {voo['aviao']}, Assentos: {voo['assentosTotais']}")
        else:
            print("Nenhum voo cadastrado.")