import uuid

class Voo:
    """Classe que representa um voo.
    Atributos:
        codigoVoo (str): código do voo
        tipoVoo (str): tipo do voo (nacional ou internacional)
        data (datetime): data do voo
        partida (Aeroporto): aeroporto de partida
        destino (Aeroporto): aeroporto de destino
        aviao (Aviao): avião do voo
        assentosTotais (int): número de assentos totais do voo
        reservas (list): lista de reservas do voo
        tripulacao (list): lista de tripulantes do voo
        
    Métodos:
        assentosLivres: retorna o número de assentos livres do voo
        str: retorna uma string com os atributos do voo
        
    Quando for instanciada, é recomendado que seus parametros sejam instancias das outras classes."""
    def __init__(self, codigoVoo, tipoVoo, data, partida, destino, aviao, assentosTotais, tripulacao = None, reservas = None):
        self.__codigoVoo = codigoVoo
        self.__tipoVoo = tipoVoo
        self.__data = data
        self.__partida = partida
        self.__destino = destino
        self.__aviao = aviao
        self.__assentosTotais = assentosTotais
        self.reservas = reservas if reservas != None else []
        self.__tripulacao = tripulacao if tripulacao != None else []

    def assentosLivres(self):
        return self.__assentosTotais - len(self.reservas)
    
    def get_aviao(self):
        return self.__aviao
    
    def get_assentos(self):
        return self.__assentosTotais
    
    def get_codigoVoo(self):
        return self.__codigoVoo
    
    def get_voo(self):
        return self.get_voo
    
    def get_tripulacao(self):
        return self.__tripulacao

    def __str__(self):
        return f"Voo: {self.__codigoVoo}\nTipo: {self.__tipoVoo}\nData: {self.__data}\nPartida: {self.__partida}\nDestino: {self.__destino}\nAvião: {self.__aviao}\nAssentos Totais: {self.__assentosTotais}\nAssentos Livres: {self.assentosLivres()}"        

class Aviao:
    """Classe que representa um avião.
    Atributos:
        modelo (str): modelo do avião
        capacidade (int): capacidade do avião
    
    Métodos:
        str: retorna uma string com apenas o modelo do avião"""
    def __init__(self, modelo, capacidade, codigoAviao = None):
        self.modelo = modelo
        self.__capacidade = capacidade
        self.__codigoAviao = codigoAviao

    def get_capacidade(self):
        return self.__capacidade
    
    def get_codigoAviao(self):
        return self.__codigoAviao
    
    def __str__(self):
        return f"{self.modelo}"

class Companhia:
    """Classe que representa uma companhia aérea.
    Atributos:
        nome (str): nome da companhia
        cnpj (str): CNPJ da companhia
        avioes (list): lista de avioes da companhia
        
    Métodos:
        cadastrarAviao: adiciona um avião à lista de avioes da companhia
        removerAviao: remove um avião da lista de avioes da companhia"""
    def __init__(self, nome, cnpj, capacidadeMaxAvioes, avioes = None):
        self.nome = nome
        self.__cnpj = cnpj
        self.__capacidadeMaxAvioes = capacidadeMaxAvioes
        self.__avioes = avioes if avioes != None else []

    def get_avioes(self):
        return self.__avioes
    
    def get_capacidadeMaxAvioes(self):
        return self.__capacidadeMaxAvioes
    
class Aeroporto:
    """Classe que representa um aeroporto.
    Atributos:
        nome (str): nome do aeroporto
        cidade (str): cidade do aeroporto
        voos (list): lista de voos do aeroporto
        
    Métodos:
        cadastrarVoo: adiciona um voo à lista de voos do aeroporto
        str: retorna uma string com o nome e a cidade do aeroporto"""
    def __init__(self, nome, cidade, capacidadeMaxVoosHora, voos = None):
        self.nome = nome
        self.cidade = cidade
        self.__capacidadeMaxVoosHora = capacidadeMaxVoosHora
        self.__voos = voos if voos != None else []

    def get_voos(self):
        return self.__voos
    
    def get_capacidadeMaxVoosHora(self):
        return self.__capacidadeMaxVoosHora
    
    def __str__(self):
        return f"{self.nome} Cidade: {self.cidade}"
    
class Reserva:
    """Classe que representa uma reserva.
    Atributos:
        passageiro (Passageiro): passageiro que fez a reserva
        voo (Voo): voo da reserva
        id (uuid): id da reserva, deve ser gerado automaticamente com a função uuid.uuid4() da biblioteca uuid"""
    def __init__(self, passageiro, voo, id = None):
        self.__passageiro = passageiro
        self.__voo = voo

    def get_passageiro(self):
        return self.__passageiro
    
    def get_voo(self):
        return self.__voo.get_codigoVoo()

class Passageiro:
    """Classe que representa um passageiro.
    Atributos:
        nome (str): nome do passageiro
        cpf (str): CPF do passageiro
        reservas (list): lista de reservas do passageiro
        
    Métodos:
        fazerReserva: faz uma reserva para o passageiro em um voo
        cancelarReserva: cancela uma reserva do passageiro em um voo
        visualizarReservas: retorna o número de reservas do passageiro"""
    def __init__(self, nome, cpf, reservas = None):
        self.nome = nome
        self.__cpf = cpf
        self.__reservas = reservas if reservas != None else []

    def fazerReserva(self, passageiro, voo):
        if voo.assentosLivres() > 0:
            id = uuid.uuid4()
            reserva = Reserva(passageiro, voo, id)
            voo.reservas.append(reserva)
            passageiro.__reservas.append(reserva)
            return f"Reserva feita com sucesso para o voo {reserva.get_voo()}."
        else:
            return "Não há assentos livres para este voo."

    def cancelarReserva(self, id):
        if len(self.__reservas) > 0:
            for i in range(len(self.__reservas)):
                if self.__reservas[i].get_id() == id:
                    self.__reservas.pop(i)
                    return f"Reserva para o voo {self.__reservas[i].get_voo()} cancelada com sucesso."
            return "Reserva não encontrada."
        else:
            return "Não há reservas para cancelar."
    
    def get_reservas(self):
        return self.__reservas
    
    def get_cpf(self):
        return self.__cpf

import csv

class OrganizadorCSV:
    contador_id = 0  # Inicializa o contador de ID

    def __init__(self):
        self.arquivo_passageiros = "passageiros.csv"
        self.arquivo_reservas = "reservas.csv"

    def proximo_id(self):
        """Retorna o próximo ID de reserva e incrementa o contador."""
        id_atual = self.contador_id
        self.contador_id += 1
        return id_atual

    def salvarPassageiro(self, passageiro):
        """Salva informações do passageiro em um arquivo CSV."""
        with open(self.arquivo_passageiros, mode='a', newline='', encoding='utf-8') as file:
            cabecalhos = ['nome', 'cpf']
            escrever_csv = csv.DictWriter(file, fieldnames=cabecalhos)

            if file.tell() == 0:  # escreve o cabeçalho se o arquivo estiver vazio
                escrever_csv.writeheader()

            escrever_csv.writerow({'nome': passageiro.nome, 'cpf': passageiro.get_cpf()})

    def carregarPassageiros(self):
        """Carrega informações de passageiros do arquivo CSV."""
        passageiros = []
        try:
            with open(self.arquivo_passageiros, mode='r') as file:
                ler_csv = csv.DictReader(file)
                for coluna in ler_csv:
                    passageiros.append({
                        'nome': coluna['nome'],
                        'cpf': coluna['cpf']
                    })
        except FileNotFoundError:
            pass
        return passageiros

    def salvarReservaPassageiro(self, reserva):
        """Salva informações da reserva em um arquivo CSV."""
        with open(self.arquivo_reservas, mode='a', newline='', encoding='utf-8') as file:
            cabecalhos = ['cpf', 'voo', 'id']
            escrever_csv = csv.DictWriter(file, fieldnames=cabecalhos)

            if file.tell() == 0:  # escreve o cabeçalho se o arquivo estiver vazio
                escrever_csv.writeheader()

            escrever_csv.writerow({
                'cpf': reserva.get_passageiro().get_cpf(),
                'voo': reserva.get_voo(),
                'id': self.proximo_id()  # usa o id atual e incrementa o contador
            })

    def carregarReservas(self):
        """Carrega informações de reservas do arquivo CSV."""
        reservas = []
        try:
            with open(self.arquivo_reservas, mode='r') as file:
                ler_csv = csv.DictReader(file)
                for coluna in ler_csv:
                    reservas.append({
                        'cpf': coluna['cpf'],
                        'voo': coluna['voo'],
                        'id': int(coluna['id'])
                    })
        except FileNotFoundError:
            pass
        return reservas

    def removerReserva(self, id):
        """Remove uma reserva com base no ID do arquivo CSV."""
        reservas = []
        with open(self.arquivo_reservas, mode='r') as file:
            ler_csv = csv.DictReader(file)
            cabecalhos = ler_csv.fieldnames
            for coluna in ler_csv:
                if coluna['id'] != str(id): # se o ID for diferente, adiciona a linha
                    reservas.append(coluna) 

        with open(self.arquivo_reservas, mode='w', newline='') as file:
            ler_csv = csv.DictWriter(file, fieldnames=cabecalhos)
            ler_csv.writeheader()
            ler_csv.writerows(reservas)

    def removerPassageiro(self, cpf):
        """Remove um passageiro com base no CPF do arquivo CSV."""
        passageiros = []
        with open(self.arquivo_passageiros, mode='r') as file:
            ler_csv = csv.DictReader(file)
            cabecalhos = ler_csv.fieldnames
            for row in ler_csv:
                if row['cpf'] != cpf:
                    passageiros.append(row)

        with open(self.arquivo_passageiros, mode='w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=cabecalhos)
            writer.writeheader()
            writer.writerows(passageiros)

class Menu:
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
            print("7. Sair")

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
                break
            else:
                print("Opção inválida. Tente novamente.")

    def cadastrar_passageiro(self):
        nome = input("Digite o nome do passageiro: ")
        cpf = input("Digite o CPF do passageiro: ")

        passageiro = Passageiro(nome, cpf)
        self.organizador.salvarPassageiro(passageiro)
        print(f"Passageiro {nome} cadastrado com sucesso.")

    def visualizar_passageiros(self):
        passageiros = self.organizador.carregarPassageiros()
        if passageiros:
            print("\nPassageiros:")
            for passageiro in passageiros:
                print(f"Nome: {passageiro['nome']}, CPF: {passageiro['cpf']}")
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
        voo_codigo = input("Digite o código do voo: ")

        passageiros = self.organizador.carregarPassageiros()
        if any(passageiro['cpf'] == cpf for passageiro in passageiros):
            voo = None  # Substitua isso com a lógica para obter o objeto Voo adequado
            if voo:
                reserva = Reserva(passageiros[cpf], voo)
                self.organizador.salvarReservaPassageiro(reserva)
                print(f"Reserva para o voo {voo_codigo} cadastrada com sucesso.")
            else:
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

# Exemplo de uso:
organizador = OrganizadorCSV()
menu = Menu(organizador)
menu.exibir_menu()