from voo.voo import Voo
from voo.pessoa import Passageiro
from voo.reserva import Reserva
from utilities.organizadorcsv import OrganizadorCSV

class MenuPassageiro:
    def __init__(self, organizador, nome, cpf, telefone):
        self.organizador = organizador
        self.nome = nome
        self.cpf = cpf
        self.telefone = telefone

    def exibir_menu(self):
        while True:
            print("\n1. Ver voos disponíveis")
            print("2. Fazer uma reserva")
            print("3. Ver suas reservas")
            print("4. Cancelar uma reserva")
            print("5. Voltar ao menu principal")

            escolha = input("Escolha uma opção: ")

            if escolha == '1':
                self.visualizar_voos()
            elif escolha == '2':
                self.fazer_reserva()
            elif escolha == '3':
                self.visualizar_reservas()
            elif escolha == '4':
                self.cancelar_reserva()
            elif escolha == '5':
                print("Saindo...")
                break
            else:
                print("Opção inválida. Tente novamente.")

    def visualizar_voos(self):
        voos = self.organizador.carregarVoos()
        if voos:
            print("\nVoos disponíveis:")
            for voo in voos:
                print(f"Código: {voo['codigo']}, Tipo: {voo['tipo']}, Data: {voo['data']}, Partida: {voo['partida']}, Destino: {voo['destino']}, Avião: {voo['aviao']}")
        else:
            print(f"Não há voos disponíveis.")

    def fazer_reserva(self):
        cpf = self.cpf
        voo_codigo = input("Digite o código do voo: ")
        assento = input("Digite o número do assento: ")

        # verifica se já tem reserva para o voo
        reservas = self.organizador.carregarReservas()
        reserva_existente = next((reserva for reserva in reservas if reserva['cpf'] == cpf and reserva['voo'] == voo_codigo), None)

        # verifica se o assento esta ocupado
        reserva_assento = next((reserva for reserva in reservas if reserva['voo'] == voo_codigo and str(reserva['assento']) == assento), None)

        if reserva_existente:
            print(f"Você já possui uma reserva para o voo {voo_codigo}.")
        elif reserva_assento:
            print(f"O assento {assento} já está ocupado.")
        else:
            voo_info = self.organizador.obterVooPorCodigo(voo_codigo)
            passageiros = self.organizador.carregarPassageiros()
            passageiro_encontrado = next((passageiro for passageiro in passageiros if passageiro['cpf'] == cpf), None)

            if passageiro_encontrado and voo_info:
                voo = Voo(voo_info['codigo'], voo_info['tipo'], voo_info['data'], voo_info['partida'], voo_info['destino'], voo_info['aviao'])
                reserva = Reserva(passageiro_encontrado, voo, assento)
                self.organizador.salvarReservaPassageiro(reserva)
                print(f"Reserva para o voo {voo_codigo} feita com sucesso.")
            elif not voo_info:
                print(f"Voo {voo_codigo} não encontrado.")
            else:
                print(f"Não foi possível realizar a reserva.")

    def visualizar_reservas(self):
        cpf = self.cpf
        reservas = self.organizador.carregarReservas()
        if any(reserva['cpf'] == cpf for reserva in reservas):
            print("\nReservas:")
            for reserva in reservas:
                if reserva['cpf'] == cpf:
                    print(f"Código do voo: {reserva['voo']}, Assento: {reserva['assento']}")
        else:
            print(f"Você não possui reservas.")

    def cancelar_reserva(self):
        cpf = self.cpf
        reservas = self.organizador.carregarReservas()

        if any(reserva['cpf'] == cpf for reserva in reservas):
            print("Suas reservas:")
            for reserva in reservas:
                if reserva['cpf'] == cpf:
                    print(f"Código do voo: {reserva['voo']}, Assento: {reserva['assento']}")

            voo_codigo = input("Digite o código do voo que deseja cancelar a reserva: ")
            assento = input("Digite o número do assento que deseja cancelar: ")

            reserva_igual = [reserva for reserva in reservas if reserva['cpf'] == cpf and reserva['voo'] == voo_codigo and str(reserva['assento']) == assento]

            if reserva_igual:
                # 
                removido = self.organizador.removerReserva(reserva_igual[0]['assento'])
                if removido:
                    print(f"Reserva para o voo {voo_codigo}, assento {assento} cancelada com sucesso.")
                else:
                    print(f"Erro ao cancelar a reserva.")
            else:
                print(f"Reserva não encontrada para o voo {voo_codigo}, assento {assento}.")
        else:
            print("Você não possui reservas.")