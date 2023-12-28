import csv
from abc import ABC, abstractmethod

class InterfaceCSV(ABC):
    @abstractmethod
    def lerCsv(self, arquivo):
        pass

    @abstractmethod
    def escreverCsv(self, arquivo, dados, cabecalhos, modo='a'):
        pass

class OrganizadorCSV(InterfaceCSV):
    """Classe para organizar as informações em arquivos CSV.
    Atributos:
        arquivo_passageiros (str): nome do arquivo CSV de passageiros
        arquivo_reservas (str): nome do arquivo CSV de reservas
        arquivo_voos (str): nome do arquivo CSV de voos
    
        O nome dos arquivos são definidos no construtor, e podem ser alterados
        """
    def __init__(self):
        self.arquivo_passageiros = "passageiros.csv"
        self.arquivo_reservas = "reservas.csv"
        self.arquivo_voos = "voos.csv"
        self.arquivo_tripulantes = "tripulantes.csv"

    def lerCsv(self, arquivo):
        """Lê um arquivo CSV e retorna uma lista de dicionários com as informações do CSV."""
        with open(arquivo, mode='r', encoding='utf-8') as file:
            ler_csv = csv.DictReader(file)
            dados = []
            for coluna in ler_csv:
                dados.append(coluna)
        return dados
    
    def escreverCsv(self, arquivo, dados, cabecalhos, modo='a'):
        """Escreve em um arquivo CSV.
            Recebe o nome do arquivo, os dados a serem escritos, os cabeçalhos e o modo de escrita.
            O modo de escrita padrão é 'a' (append)."""
        with open(arquivo, mode=modo, newline='', encoding='utf-8') as file:
            escreverCsv = csv.DictWriter(file, fieldnames=cabecalhos)

            if file.tell() == 0:
                escreverCsv.writeheader()

            escreverCsv.writerow(dados)

    def salvarPassageiro(self, passageiro):
        """Salva informações do passageiro em um arquivo CSV.
           Recebe um objeto de Passageiro como parâmetro."""
        cabecalhos = ['nome', 'cpf', 'telefone']
        dados = {'nome': passageiro.nome, 'cpf': passageiro.get_cpf(), 'telefone': passageiro.telefone}
        
        self.escreverCsv(self.arquivo_passageiros, dados, cabecalhos, modo='a')

    def carregarPassageiros(self):
        """Carrega informações de passageiros do arquivo CSV.
            Retorna uma lista de dicionários com as informações do csv."""
        return self.lerCsv(self.arquivo_passageiros)

    def salvarReservaPassageiro(self, reserva):
        """Salva informações da reserva em um arquivo CSV.
            Recebe um objeto de Reserva como parâmetro.
            As verificações para o assento e voo devem ser feitas no menu."""
        cabecalhos = ['cpf', 'voo', 'assento']
        dados = {'cpf': reserva.get_passageiro()['cpf'], 'voo': reserva.get_voo(), 'assento': reserva.get_assento()}
        
        self.escreverCsv(self.arquivo_reservas, dados, cabecalhos, modo='a')

    def carregarReservas(self):
        """Carrega informações de reservas do arquivo CSV.
            Retorna uma lista de dicionários com as informações do csv."""
        return self.lerCsv(self.arquivo_reservas)

    def removerReserva(self, assento):
        """Remove uma reserva com base no ID (assento) do arquivo CSV.
            Retorna True se a reserva foi removida e False caso contrário
            assim podemos usar um if para verificar se a reserva foi removida.
            O ID agora é o assento."""
        reservas = []
        removida = False
        try:
            with open(self.arquivo_reservas, mode='r', encoding='utf-8') as file:
                ler_csv = csv.DictReader(file)
                cabecalhos = ler_csv.fieldnames
                for coluna in ler_csv:
                    if coluna['assento'] != str(assento):
                        reservas.append(coluna) 
                    else:
                        removida = True

            with open(self.arquivo_reservas, mode='w', newline='') as file:
                ler_csv = csv.DictWriter(file, fieldnames=cabecalhos)
                ler_csv.writeheader()
                ler_csv.writerows(reservas)

            return removida
        except FileNotFoundError:
            pass  

    def removerPassageiro(self, cpf):
        """Remove um passageiro com base no CPF do arquivo CSV.
            Não possui retorno, apenas remove o passageiro do arquivo CSV."""
        passageiros = []
        with open(self.arquivo_passageiros, mode='r', encoding='utf-8') as file:
            ler_csv = csv.DictReader(file)
            cabecalhos = ler_csv.fieldnames
            for row in ler_csv:
                if row['cpf'] != cpf:
                    passageiros.append(row)

        with open(self.arquivo_passageiros, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=cabecalhos)
            writer.writeheader()
            writer.writerows(passageiros)

    def salvarVoo(self, voo):
        """Salva informações do voo em um arquivo CSV.
            Recebe um objeto de Voo como parâmetro."""
        cabecalhos = ['codigo', 'tipo', 'data', 'partida', 'destino', 'aviao']
        dados = {'codigo': voo.get_codigoVoo(), 'tipo': voo.get_tipoVoo(), 'data': voo.get_dataVoo(), 'partida': voo.get_partida(), 'destino': voo.get_destino(), 'aviao': voo.get_aviao()}
        
        self.escreverCsv(self.arquivo_voos, dados, cabecalhos, modo='a')
    
    def carregarVoos(self):
        """Carrega informações de voos do arquivo CSV.
            Retorna uma lista de dicionários com as informações do csv."""
        try:
            return self.lerCsv(self.arquivo_voos)
        except FileNotFoundError:
            return "O arquivo não existe."
    
    def obterVooPorCodigo(self, codigo):
        """Carrega informações de um voo específico do arquivo CSV.
            Se encontrar o voo, retorna ele."""
        voos = self.carregarVoos()
        for voo in voos:
            if voo['codigo'] == codigo:
                return voo
        return None
    
    def salvarTripulante(self, tripulante):
        """Salva informações do tripulante em um arquivo CSV.
            Recebe um objeto de Tripulante como parâmetro."""
        cabecalhos = ['nome', 'cpf', 'funcao', 'voo_codigo']
        dados = {'nome': tripulante.nome, 'cpf': tripulante.get_cpf(), 'funcao': tripulante.get_funcao(), 'voo_codigo': tripulante.voo}
        
        self.escreverCsv(self.arquivo_tripulantes, dados, cabecalhos, modo='a')

    def carregarTripulantes(self):
        """Carrega informações de tripulantes do arquivo CSV.
            Retorna uma lista de dicionários com as informações do csv."""
        tripulantes = []
        try:
            with open(self.arquivo_tripulantes, mode='r', encoding='utf-8') as file:
                ler_csv = csv.DictReader(file)
                for coluna in ler_csv:
                    voo_codigo = coluna['voo_codigo']
                    voo = self.obterVooPorCodigo(voo_codigo) if voo_codigo else None

                    tripulantes.append({
                        'nome': coluna['nome'],
                        'cpf': coluna['cpf'],
                        'funcao': coluna['funcao'],
                        'voo': voo
                    })
        except FileNotFoundError:
            pass
        return tripulantes

    def removerTripulante(self, cpf):
        """Remove um tripulante com base no CPF do arquivo CSV.
            Não possui retorno, apenas remove o tripulante do arquivo CSV."""
        tripulantes = []
        with open(self.arquivo_tripulantes, mode='r', encoding='utf-8') as file:
            ler_csv = csv.DictReader(file)
            cabecalhos = ler_csv.fieldnames
            for row in ler_csv:
                if row['cpf'] != cpf:
                    tripulantes.append(row)

        with open(self.arquivo_tripulantes, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=cabecalhos)
            writer.writeheader()
            writer.writerows(tripulantes)