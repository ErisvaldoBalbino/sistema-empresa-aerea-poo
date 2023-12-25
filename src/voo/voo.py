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
    
    def get_tipoVoo(self):
        return self.__tipoVoo
    
    def get_data(self):
        return self.__data
    
    def get_partida(self):
        return self.__partida

    def get_destino(self):
        return self.__destino

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